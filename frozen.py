#-*-coding:utf-8-*-

import requests
import telepot
from bs4 import BeautifulSoup
from datetime import datetime

now = datetime.now()
token = "1042804802:AAG4SbkWhnOyvor8l6SDFgZ8bae1fqljfq4"
bot = telepot.Bot(token)
my_id = "906326133"

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20191121'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
list = soup.select('.info-hall')

if '겨울' in html and 'IMAX' in str(list):
    bot.sendMessage(chat_id='906326133', text="겨울왕국 2 IMAX 예매 열림")
else:
    bot.sendMessage(chat_id='906326133', text="알리미 정상 작동 중 !!")
