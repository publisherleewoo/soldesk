from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  #크롬 브라우저 오픈
driver.get("https://www.melon.com/chart/index.htm")  # 크롤링할 웹페이지 주소.  


_as = driver.find_elements(By.CSS_SELECTOR,".rank01")  # .rank01  =>css 선택자


for a in _as:
 
    print(a.text)


driver.quit()