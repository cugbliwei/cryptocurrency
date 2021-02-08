import requests


data = {'coin_name': 'BTC'}
# resp = requests.post('http://127.0.0.1:80/otc/sumary', data=data)
resp = requests.post('http://47.100.172.107:80/otc/sumary', data=data)
print(resp.json())
