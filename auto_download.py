
import re
import requests

from bs4 import BeautifulSoup

from bdy_control import download_link

# 填入天天美剧的下载页面地址
url = "http://www.msj1.com/archives/5238.html"

response = requests.get(url, headers={'user-agent': 'Mozilla/5.0'}, timeout=30)

print(response.status_code)

print(response.reason)

for name,value in response.headers.items():
    print("%s:%s" % (name, value))

with open("test.html", "wb") as f:
    f.write(response.content)

soup = BeautifulSoup(response.content, "html.parser")

'''
with open("test.html", "r", encoding='utf-8') as f:
    text = f.read()
    
soup = BeautifulSoup(text, "html.parser")
'''

for link in soup.find_all(href=re.compile("^ed2k")):
    print('开始下载：%s' %(link.get_text()))
    download_link(link.get('href'))

print('添加离线下载任务完成！！！')
