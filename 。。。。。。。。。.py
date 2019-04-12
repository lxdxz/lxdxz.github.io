import requests
from datetime import datetime
dd = datetime.now()
url = 'https://www.ssrenji.com'
a = 1
b = 0
c = 0
try:
    print('现在是',dd)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    while a == 1:
        response = requests.get(url,headers=headers)
        resp = str(response)
        if resp == '<Response [200]>':
            b+=1
            print('第',b,'次请求成功！')
            print('======================')
            if b == 10:
                break;


        if not resp == '<Response [200]>':
            c+=1
            print('第',c,'次请求失败')
            print('---------------------')
            if c == 20:
                print('请求失败次数过多，停止请求')
                print('========================\n========================\n========================')
                break;
    print('共爬取',b,'次!')
except SyntaxError:
    print()
        


    
    
