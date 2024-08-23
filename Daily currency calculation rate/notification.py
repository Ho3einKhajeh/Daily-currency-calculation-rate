from kavenegar import *
from config import rules


def send_sms(text):
    try:
        api = KavenegarAPI('')
        params = {
            'sender': '1000689696',
            'receptor': rules['notification']['reciver'],
            'message': text
        }
        response = api.sms_send(params)
        print(str(response))
    except APIException as e:
        print(str(e))
    except HTTPException as e:
        print(str(e))
