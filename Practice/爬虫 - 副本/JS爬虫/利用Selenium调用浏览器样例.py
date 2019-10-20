from selenium import webdriver

browser = webdriver.Chrome()  # 调用本地的Chrome浏览器
browser.get('http://www.aqistudy.cn/historydata/daydata.php?city=%E5%8C%97%E4%BA%AC&amp;month=201606')  # 请求页面，会打开一个浏览器窗口
html_text = browser.page_source  # 获得页面代码
#browser.quit()  # 关闭浏览器
print(html_text)

