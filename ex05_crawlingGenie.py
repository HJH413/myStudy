from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# 자신이 사용하는 크롬의 ver 확인하고 크롬드라이버 설치하기
# https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome('./webdriver/chromedriver.exe')

# genie 차트 크롤링하기
urlList = ['https://www.genie.co.kr/chart/top200',
           'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20220630&hh=15&rtm=Y&pg=2']
songs = []
songDataList = []
rank = 1
for url in urlList:
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    songs.extend(soup.select('table.list-wrap > tbody > tr'))

print(len(songs))
for song in songs:
    title = song.select_one('td.info > a.title').text.strip()
    singer = song.select_one('td.info > a.artist').text.strip()
    songDataList.append(['genie', rank, title, singer])
    rank += 1
    print(rank, title, singer, sep='|')

    print(songDataList)
    #
    columns = ['서비스', '순위', '타이틀', '가수']
    pd_data = pd.DataFrame(songDataList, columns=columns)
    pd_data.to_excel('./genies.xlsx', index=False)
