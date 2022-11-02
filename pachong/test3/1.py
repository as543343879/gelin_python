#-*- coding:utf-8 -*-

# 主要用来测试Selenium 使用PhantomJS

#导入webdriver
from selenium import webdriver
import time

# 想要调用键盘按键操作需要导入keys包
from selenium.webdriver.common.keys import Keys

# 调用环境变量指定的PhantomJS浏览器创建浏览器对象。
driver = webdriver.PhantomJS()
driver.set_window_size(1366,768)

#如果没有在环境变量指定PhantomJS位置
driver = webdriver.PhantomJS(execute_path="D:/softwareMajor/phantomjs-2.1.1-windows/bin/phantomjs.exe")

# get方法会一直等到页面加载，然后才会继续执行程序，通常测试会在这里选择time.sleep(2)

driver.get("http://www.baidu.com/")

# 获取页面名为wrapper的id标签的文本内容
data = driver.find_element_by_id('wrapper').text

print(data)

print(driver.title)

# 生成页面快照并保存
driver.save_screenshot("baidu.png")

# id="kw" 是百度搜索输入框，输入字符串 "长城"
driver.find_element_by_id('kw').send_keys('长城')

# id="su"是百度搜索按钮，click()是模拟点击
driver.find_element_by_id('su').click()

#获取新的页面快照
driver.save_screenshot("长城.png")
#打印网页渲染后的源代码
print(driver.page_source)

# 获取当前页面的Cookie
print(driver.get_cookies())

# ctrl + a 全选输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
#ctrl+x剪切输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

#输入框重新输入内容
driver.find_element_by_id('kw').send_keys('itcast')

#模拟Enter回车键
driver.find_element_by_id('su').send_keys(Keys.RETURN)
time.sleep(5)

#生成新的页面快照
driver.save_screenshot('itcast.png')

#获取当前url
print(driver.current_url)

driver.quit()