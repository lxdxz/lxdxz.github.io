import requests
from bs4 import BeautifulSoup
i = 1
b = 0
while i == 1:
    a = '百度'
    url = 'http://www.yunpangou.com/21547805832407'
    headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    response = requests.get(url)
    print(response)
    b+=1
    print(b)
    
