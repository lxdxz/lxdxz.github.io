import requests
url = 'http://localhost:8888/'
headers = {
    'User-Agent':'niubidong'}
a = 1
while a == 1:
    
    s = requests.get(url,headers=headers)
    print(s)
