from selenium import webdriver
import time

url = 'https://www.douban.com/'
driver = webdriver.Chrome()
driver.get(url)

driver.implicitly_wait(10)

# 第一个页面的数据获取
## 浏览器中右击标签，可直接 copy xpath
### 通过 xpath 找到标签
# book = driver.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click()
# 通过链接找标签
book = driver.find_element_by_link_text('豆瓣读书').click()
time.sleep(3)

# 获取窗口数量，得到列表
windows = driver.window_handles
print(windows)
# 切换到第二个窗口
driver._switch_to.window(windows[1])

# 第二个页面的数据获取（如果不切换，还停留在上一个页面）
music = driver.find_element_by_xpath('//*[@id="db-global-nav"]/div/div[3]/ul/li[4]/a')
print(music)
music.click()
driver.quit()
time.sleep(2)