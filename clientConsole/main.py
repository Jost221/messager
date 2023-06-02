import requests

# name = input('input your id')
name = '1'
a = requests.get('http://127.0.0.1:8000/', params=f'id={name}')

with open('clientConsole/page.html', 'w') as f:
    f.write(a.text)