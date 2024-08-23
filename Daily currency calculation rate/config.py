BASE_PATH = ''
API_KEY = ''
url = BASE_PATH + API_KEY
EMAIL_RECIVER = ""
rules = {
    'archive': True,
    'email': {
        'reciver': '',
        'enable': True,
        'preferred': ['BTC', 'IRR', 'IQD', 'USD', 'CAD', 'AED']
    },
    'notification': {
        'enable': True,
        'reciver': '',
        'preferred': {
            'BTC': {'min': '0.000101', 'max': '0.000110'},
            'IRR': {'min': '45000', 'max': '50000'}
        }
    }
}
