import datetime
import re
import os
import requests
import schedule
import time
from bs4 import BeautifulSoup

''''''
#カレントディレクトリの移動 →batファイルで実行することで解決
#os.chdir("scraping")
#current = os.getcwd()
#print(current)

#時間取得
today = datetime.date.today()

#ファイル名を日付ごとに設定
file_name = str(today) + "_news.txt"

#Yahoo!newsを取得
url = 'https://www.yahoo.co.jp/'
res = requests.get(url)

#BeautifulSoupに読み込ませる
soup = BeautifulSoup(res.text, "html.parser")

#elems = soup.find_all("a") #タグ<a>に含まれるすべての要素

#文をdata_listへ
data_list = soup.find_all(href = re.compile("news.yahoo.co.jp/pickup"))

#ファイルへ書き込み　タイトルとURL
news = open(file_name, 'w', encoding = "utf-8")
for data in data_list:
    #print(data.span.string)
    #print(data.attrs['href'])
    news.write(str(data.span.string + "\n" + data.attrs['href']) + "\n")

news.close()