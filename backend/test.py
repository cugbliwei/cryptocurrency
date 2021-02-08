import requests


data = {'trade_type': 'sell', 'coin_name': 'BTC'}
resp = requests.post('http://127.0.0.1:8081/otc/sumary', data=data)
print(resp.json())
