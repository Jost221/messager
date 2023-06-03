import requests

# name = input('input your id')
name = '1'
a = requests.get('http://127.0.0.1:8000/create', params=f'id={name}')
print(a.text)