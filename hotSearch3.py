import datetime
import mysql.connector
import requests
from bs4 import BeautifulSoup

PREFIX = 'https://s.weibo.com'

r = requests.get('https://s.weibo.com/top/summary')
html = r.text
soup = BeautifulSoup(html)
eles = soup.select('.td-02 a')

config = {
    'user': 'root',
    'password': 'root',
    'host': '172.22.64.1',
    'database': 'mydb',
}
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

today = datetime.date.today()

insert = "insert into mydb.t_search_hot (link, title, date) values (%s, %s, %s)"
repeat = "select count(1) from mydb.t_search_hot where date=%s and title=%s"

for ele in eles:
    link = ele.get('href')
    if link == 'javascript:void(0);':
        link = 'https://s.weibo.com' + ele.get('href_to')
    else:
        link = PREFIX + link
    title = ele.getText()
    cursor.execute(repeat, (today, title))
    if cursor.fetchone()[0] == 0:
        cursor.execute(insert, (link, title, today))

conn.commit()

cursor.close()
conn.close()