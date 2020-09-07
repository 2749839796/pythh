from selenium import webdriver
import time

username = '2744255833@qq.com'
pwd = '2744255833aa'

url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
driver = webdriver.Chrome()
driver.get(url)

driver.implicitly_wait(10)

# 输用户名
driver.find_element_by_id('email').send_keys(username)
time.sleep(2)
# 输密码
driver.find_element_by_id('pwd').send_keys(pwd)
time.sleep(2)
# 在pycharm中手动输验证码
code = input('验证码>>>')
driver.find_element_by_id('code').send_keys(code)
time.sleep(2)
# 点击登录
driver.find_element_by_id('denglu').click()
print('登陆成功')
time.sleep(10)
driver.close()