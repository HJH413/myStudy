from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# 자신이 사용하는 크롬의 ver 확인하고 크롬드라이버 설치하기
# https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome('./webdriver/chromedriver.exe')

# 멜론 차트 크롤링하기
url = "https://www.melon.com/chart/index.htm"
driver.get(url)
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# songs = soup.select('tbody > tr')
songs = driver.find_elements_by_css_selector('table > tbody > tr')
# print(len(songs))
songDataList = []
rank = 1
for song in songs:
    title = song.find_elements_by_css_selector('div.ellipsis.rank01 > span > a')[0].text
    singer = song.find_elements_by_css_selector('div.ellipsis.rank02 > a')[0].text
    songDataList.append(['Melon', rank, title, singer])
    rank += 1
    print(title, singer, sep='|')

print(songDataList)

columns = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(songDataList, columns=columns)
pd_data.to_excel('./melon.xlsx', index=False)