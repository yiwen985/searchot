import datetime
import requests
from bs4 import BeautifulSoup

PREFIX = 'https://s.weibo.com'

r = requests.get('https://s.weibo.com/top/summary')
html = r.text

soup = BeautifulSoup(html)

eles = soup.select('.td-02 a')

for ele in eles:
    print(ele.get('href'), ele.string, datetime.date.today())