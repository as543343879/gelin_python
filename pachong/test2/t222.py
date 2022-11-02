# 创建浏览器对象

# driver = webdriver.Chrome()

# 爬取今日头条热点新闻标题
from msedge.selenium_tools.service import Service
from selenium import webdriver
# from msedge.selenium_tools import Edge, EdgeOptions

from selenium.webdriver.edge.options import Options

# 启动浏览器
# url = 'https://www.toutiao.com'

url = 'https://sports.ladbrokes.com/competitions/football/english/premier-league'


from selenium.webdriver.edge.options import Options

options = Options()
 # options.add_argument("headless")
options.add_argument('headless')
options.add_argument('no-sandbox')
options.add_argument('disable-dev-shm-usage')
# options = EdgeOptions()
# options.use_chromium = True
# options.add_argument("headless")

# 设置好应用扩展
extension_path = 'C:/Users/lizhi/Downloads/Ghelper-v2.6.2/Ghelper-v2.6.2.crx'
options.add_extension(extension_path)
options.add_argument(r'user-data-dir=C:\Users\lizhi\AppData\Local\Microsoft\Edge\User Data')


# from selenium.webdriver.edge.service import Service
service = Service(r'C:\Users\lizhi\Downloads\edgedriver_win64\msedgedriver.exe', verbose=True)

driver = webdriver.Edge(service=service, options=options)


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
