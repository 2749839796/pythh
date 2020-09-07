from selenium import webdriver

url = 'https://www.baidu.com/'

# driver有驱动的意思，驱动chrome浏览器.path为驱动所在路径
driver = webdriver.Chrome(executable_path=r'D:\python\chromedriver.exe')
driver.get(url)

# 如果驱动程序在python根目录，可以省略路径
# driver = webdriver.Chrome()


# 窗口最大化
driver.maximize_window()
# 窗口为400x400
# driver.set_window_size(400, 400)

# 截屏并保存
driver.save_screenshot(r'C:\Users\ASUS PC\Desktop\1.png')

# 关闭当前页面
driver.close()
# 关闭所有页面
# driver.quit()