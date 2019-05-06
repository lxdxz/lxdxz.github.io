import requests
from lxml import etree
def get_main_page() :
    total = []
    url = 'https://book.douban.com/top250?start=0'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    r = requests.get(url,headers=headers)
    rt = r.text
    file = open('E://text.html','w',encoding='utf-8')
    file.write(rt)
    file.close()
    html = etree.parse('./text.html' , etree.HTMLParser())
    result = html.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tbody/tr/td[2]/div[1]/span/text()')
    print(result)
    total.append({
        'finnal':result
    })
    print(total)
get_main_page()

