import requests

# name = input('input your id')
params = {
    'name' : 2,
    'dialog' : 'biba',
    'message' : 'biiiiiiiiiiiiba',
}

a = requests.post('http://127.0.0.1:8000/message', json=params)
if a.status_code != 200:
    with open('./clientConsole/page.html', 'w', encoding='utf-8') as f:
        f.write(str(a.text))
print(a.text)