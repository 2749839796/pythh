from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time

url = 'http://news.mtime.com/2020/03/08/1601614.html'

# 取消页面内的声音
## 实例化，得到一个对象
options = ChromeOptions()
options.add_argument('--mute-audio')
driver = webdriver.Chrome(options = options)
driver.get(url)

driver.implicitly_wait(10)

# js 代码，在浏览器控制滚动条，宽200，高300
js = 'window.scrollTo(200,300)'
# 到达页面最底部
# js = 'window.scrollTo(0,document.body.scrollHeight)'
driver.execute_script(js)

driver.find_element_by_xpath('//*[@id="playbtn"]/i').click()

time.sleep(15)
driver.close()
