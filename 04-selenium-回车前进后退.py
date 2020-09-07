from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.baidu.com/'
driver = webdriver.Chrome()
driver.get(url)

driver.implicitly_wait(10)

driver.find_element_by_id('kw').send_keys('mate 30')
# 只有按钮才能回车，其他标签得用click()
driver.find_element_by_id('su').send_keys(Keys.ENTER )

time.sleep(3)
# 后退
driver.back()
time.sleep(2)
# 前进
driver.forward()
time.sleep(2)
driver.close()
