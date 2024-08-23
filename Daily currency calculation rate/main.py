from datetime import datetime
import requests
import json
from khayyam import JalaliDatetime
from mail import send_smtp_email
from config import url, rules
from notification import send_sms


def get_rates():
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def archive(filename, rates):
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))


def send_mail(timestamp, rates):
    now = JalaliDatetime(datetime.now()).strftime('%y-%B-%d  %A %H:%M')
    subject = f'{timestamp} - {now} - rates:'

    if rules['email']['preferred'] is not None:
        tmp = dict()
        for exc in rules['email']['preferred']:
            tmp[exc] = rates[exc]
        rates = tmp

    text = json.dumps(rates)

    send_smtp_email(subject, text)


def send_notification(msg):
    now = JalaliDatetime(datetime.now()).strftime('%y-%B-%d  %A %H:%M')
    msg += now
    send_sms(msg)


def check_notify_rules(rates):
    preferred = rules['notification']['preferred']
    msg = ''
    for exc in preferred.keys():
        if rates[exc] <= float(preferred[exc]['min']):
            msg += f'{exc}   reached min :{rates[exc]}'
        if rates[exc] >= float(preferred[exc]['max']):
            msg += f'{exc}   reached max :{rates[exc]}'
        return msg


if __name__ == '__main__':
    res = get_rates()
    if rules['archive']:
        archive(res['timestamp'], res['rates'])
    if rules['email']['enable']:
        send_mail(res['timestamp'], res['rates'])
    if rules['notification']['enable']:
        notification_msg = check_notify_rules(res['rates'])
        if notification_msg:
            send_notification(notification_msg)
