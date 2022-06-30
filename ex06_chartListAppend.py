from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# KeyError: "There is no item named 'xl/sharedStrings.xml' in the archive"
# 위의 에러 발생시 엑셀파일을 수동으로 다시 저장해야함
excel_names = ['./melon.xlsx', './bungs.xlsx', './genies.xlsx']
append_data = pd.DataFrame()
for name in excel_names:
    print(name)
    pd_data = pd.read_excel(name)
    print(pd_data)
    append_data = append_data.append(pd_data)

print(append_data.info())
append_data.to_excel('./total.xlsx', index=False)
