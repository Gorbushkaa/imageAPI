import requests
data = {'h': 500,
        'w': 300,
        'name': '/image.jpg'}
url = 'http://127.0.0.1:5000/api/'
requests.post(url, json=data)