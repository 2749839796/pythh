from selenium import webdriver
import time

class YunSpider(object):

    # 初始化的属性，在以后的函数可以直接调用
    def __init__(self, url):
        # 初始化网址
        self.url = url
        # 打开浏览器
        self.driver = webdriver.Chrome()

    # 获取数据
    def getContent(self):
        # 打开网址
        self.driver.get(self.url)
        # 先进入IFrame，0代表第一个
        ## IFrame相当于把网页装进盒子，想要进行操作得先进房子
        self.driver.switch_to_frame(0)
        js = 'window.scrollBy(0,8000)'
        self.driver.execute_script(js)

        # 获取数据并翻页
        for page in range(10):
            ## 获取数据
            itms = self.driver.find_elements_by_xpath('//div[@class="cmmts j-flag"]/div[@class="itm"]')
            # print(itms)
            for itm in itms:
                # user = itm.find_element_by_xpath('./div[2]/div[1]/div/a').text
                user = itm.find_element_by_xpath('.//a[@class="s-fc7"]').text

                # content = itm.find_element_by_xpath('./div[2]/div[1]/div').text
                content = itm.find_element_by_xpath('.//div[@class="cnt f-brk"]').text
                # print(user,'------',content)

                # 传入给saveData函数,位置传参
                # self.saveData(user, content)
                YunSpider.saveData(user,content)

            ## 翻页
            nextpage = self.driver.find_element_by_link_text('下一页')
            nextpage.click()
            time.sleep(1)
            # page 从0开始
            print('page%d'%(page+2))

    # 保存数据
    @staticmethod
    def saveData(user,content):
        # 需手动创建文件
        with open(r'C:\Users\ASUS PC\Desktop\yun.txt',mode = 'a', encoding = 'utf-8') as f:
            f.write(user + ' :' + content + '\n')

if __name__ == '__main__':
    url = 'https://music.163.com/#/song?id=1429908253'
    yun = YunSpider(url)
    yun.getContent()