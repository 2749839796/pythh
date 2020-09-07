from selenium import webdriver

url = 'https://www.dushu.com/book/1163_1.html'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)

f = open(r'C:\Users\ASUS PC\Desktop\books.txt', mode = 'a', encoding = 'utf-8')
for page in range(1,101):
    # 进度条滑到最底部，否则因未刷新出页面而找不到元素，报错
    ## 滑到最底部
    js = 'window.scrollTo(0,document.body.scrollHeight)'
    driver.execute_script(js)

    # 注意 elements可以接收很多元素，element只能接收一个元素
    books = driver.find_elements_by_xpath('//div[@class="bookslist"]/ul/li')
    print(books)
    for book in books:
        title = book.find_element_by_xpath('.//h3/a').text
        author = book.find_element_by_xpath('./div/p[1]').text
        content = book.find_element_by_xpath('./div/p[2]').text
        # print(title)
        # print(author)
        # print(content)
        f.write('《' + title+ '》' + '  ' + author + '\n' + content + '\n')
    print('page%d'%page)

    # 上一页和下一页按钮的class相同，但第一页只有下一页按钮
    if page == 1:
        nextpage = driver.find_element_by_xpath('//div[@class="pages"]/a[@class="disabled"]')
    else:
        nextpage = driver.find_element_by_xpath('//div[@class="pages"]/a[@class="disabled"][2]')
    nextpage.click()

driver.close()
f.close()