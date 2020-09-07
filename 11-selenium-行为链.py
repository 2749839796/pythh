from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

url = 'https://www.baidu.com'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)

# 输入框
input_tag = driver.find_element_by_id('kw')
# 搜索按钮
sou_button = driver.find_element_by_id('su')

# 编写行为链
# 获取对象
actions = ActionChains(driver)
# 移动到标签
actions.move_to_element(input_tag)
# 标签内输入内容
actions.send_keys_to_element(input_tag, 'python')
actions.move_to_element(sou_button)
actions.click(sou_button)

# 根据行为链的顺序依次执行
actions.perform()