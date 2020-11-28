from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

a=input("검색할 키워드를 입력하세요 : ")
driver = webdriver.Chrome()
driver.get('https://www.google.co.kr/imghp?hl=ko')
elem = driver.find_element_by_name("q")
elem.send_keys(a)
elem.send_keys(Keys.RETURN)
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

count = 0
for image in images:
    image.click()
    time.sleep(2)
    imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
    urllib.request.urlretrieve(imgUrl, "imgfile/" + a + str(count) + ".jpg")
    count += 1
    if count == 5:
        break
#browser.quit()