from selenium import webdriver

# 该网址能查看访问的ip
url = 'http://httpbin.org/ip'

# !!! 代理需有效，否则浏览器显示网络连接超时！！！
# ip检测网址：http://www.xdaili.cn/monitor
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://123.171.5.81:8118")

driver = webdriver.Chrome(chrome_options=options)
driver.get(url)
driver.implicitly_wait(10)

