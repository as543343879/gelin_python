from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

# 创建浏览器对象

# driver = webdriver.Chrome()

# 爬取今日头条热点新闻标题
from selenium import webdriver
import time

# 启动浏览器
# url = 'https://www.toutiao.com'

url = 'https://sports.ladbrokes.com/competitions/football/english/premier-league'

chrome_options = webdriver.ChromeOptions()

# 设置好应用扩展
extension_path = 'C:/Users/lizhi/Downloads/Ghelper-v2.6.2/Ghelper-v2.6.2.crx'
chrome_options.add_extension(extension_path)
#
chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

chrome_options.add_argument(r'user-data-dir=C:\Users\lizhi\AppData\Local\Google\Chrome\User Data')
# chrome_options.add_experimental_option('useAutomationExtension', False)
# chrome_options.add_argument(r'user-data-dir=C:\Users\lenovo\AppData\Local\Google\Chrome\User Data')



driver = webdriver.Chrome(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',chrome_options=chrome_options)

# driver = webdriver.Chrome("chromedriver.exe")



driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()  # 最大化窗口
driver.implicitly_wait(10)
driver.find_element_by_link_text('热点').click()  # 点击热点
driver.implicitly_wait(10)

title_list = []


def scoll():  # 滚动页面
    # driver.execute_script("window.scrollTo(0,1000);")
    # time.sleep(1)
    name = driver.find_elements_by_class_name("container-inner-content")
    print(name)


# 运行scoll函数
scoll()
print(title_list)  # 输出结果
