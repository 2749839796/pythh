from selenium import webdriver
from PIL import Image

url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'

driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)

# 窗口大小不同，位置也不同
driver.maximize_window()
png = driver.find_element_by_id('imgCode')
# 保存窗口截屏
driver.save_screenshot(r'C:\Users\ASUS PC\Desktop\img.png')

# 获取png左上角的坐标(x,y)
loc = png.location
# 获取png的高，宽
size = png.size
print(loc,size)

# 打开文件，截取的区域（矩形根据左上角和右下角即可确定区域）
image = Image.open(r'C:\Users\ASUS PC\Desktop\img.png')
# 网页坐标
# rec = (loc['x'],loc['y'],loc['x']+size['width'],loc['y']+size['height'])
# 本地坐标(前面两个为左上角，后面两个为右下角)
rec = (480,260,555,290)
captcha = image.crop(rec)

# 显示截取结果
captcha.show()
# 保存截取的区域
captcha.save(r'C:\Users\ASUS PC\Desktop\image.png')
driver.close()

'''网页中某些区域（png）的位置和本地图片中某些区域(png)的位置不一样！！！
   根据网页中的坐标截取会截取不到，因为我们是把图片保存在本地，再打开截取某些区域
   把保存的窗口截屏用画图软件打开，分别找（png）左上角和右下角的坐标替换掉网页坐标
'''