from selenium import webdriver
from PIL import Image
import pytesseract
import time

url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'

# 获取验证码
def get_captcha():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    # 窗口大小不同，位置也不同
    driver.maximize_window()
    png = driver.find_element_by_id('imgCode')
    # 保存窗口截屏
    driver.save_screenshot(r'C:\Users\ASUS PC\Desktop\img.png')
    image = Image.open(r'C:\Users\ASUS PC\Desktop\img.png')
    rec = (480,260,555,290)
    captcha = image.crop(rec)
    # 保存截取的区域
    captcha.save(r'C:\Users\ASUS PC\Desktop\image.png')
    return driver

# 识别验证码
def recognize_captcha():
    captcha = Image.open(r'C:\Users\ASUS PC\Desktop\image.png')
    # 把图片灰度化(带有颜色的验证码难识别)
    gray = captcha.convert('L')
    # gray.show()

    # 颜色数据
    data = gray.load()
    # print(data)

    w,h = captcha.size
    # print(w,h)
    # 遍历每一个像素点，并对其修改
    ## 像素点<120 改为黑，像素点>120 改为白
    for x in range(w):
        for y in range(h):
            # 0为纯黑，255为纯白
            # print(data[x,y])
            if data[x,y] < 120:
                data[x,y] = 0
            else:
                data[x,y] = 255
    # gray.show()
    code = pytesseract.image_to_string(gray)
    print(code)
    return code

# 登录
def login(driver,code):
    # 输用户名
    driver.find_element_by_id('email').send_keys('2744255833@qq.com')
    # 输密码
    driver.find_element_by_id('pwd').send_keys('2744255833aa')
    # 输验证码
    driver.find_element_by_id('code').send_keys(code)
    time.sleep(2)
    # 点击登录
    driver.find_element_by_id('denglu').click()
    time.sleep(10)

if __name__ == '__main__':
    driver = get_captcha()
    code = recognize_captcha()
    login(driver,code)