import requests


'''
data = {'coin_name': 'BTC'}
resp = requests.post('http://47.100.172.107:80/otc/origin', data=data)
print(resp.json())
'''


'''
data = {'username': 'admin', 'password': 'abc123'}
resp = requests.post('http://47.100.172.107:80/otc/user/get', data=data)
print(resp.json())
'''

data = {'coin_name': 'USDT', 'nickname': '环球资本'}
resp = requests.post('http://47.100.172.107:80/otc/rank', data=data)
print(resp.json())
