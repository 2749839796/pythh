from selenium import webdriver
import time

url = 'https://www.taobao.com/'
driver = webdriver.Chrome()
driver.get(url)

# 最多等10秒（如果1秒就加载出页面，则执行后面的代码，相当于等1秒）
driver.implicitly_wait(10)

# 找到搜索框并输入数据（mac）
driver.find_element_by_xpath('//input[@id="q"]').send_keys('mac')

# 找到搜索按钮，并点击
driver.find_element_by_xpath('//button[@class="btn-search tb-bg"]').click()

time.sleep(3)
driver.close()