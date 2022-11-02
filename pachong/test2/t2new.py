from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

# 创建浏览器对象

from selenium import webdriver
import time

# 启动浏览器
# url = 'https://www.toutiao.com'

url = 'https://sports.ladbrokes.com/competitions/football/english/premier-league'

chrome_options = webdriver.ChromeOptions()

# 设置好应用扩展
# extension_path = 'C:/Users/lizhi/Downloads/Ghelper-v2.6.2/Ghelper-v2.6.2.crx'
# chrome_options.add_extension(extension_path)
#
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
#
# chrome_options.add_argument(r'user-data-dir=C:\Users\lizhi\AppData\Local\Google\Chrome\User Data')
# chrome_options.add_experimental_option('useAutomationExtension', False)
# chrome_options.add_argument(r'user-data-dir=C:\Users\lenovo\AppData\Local\Google\Chrome\User Data')


service = Service(r'C:\Users\lizhi\Downloads\chromedriver_win32 (1)\chromedriver.exe')

driver = webdriver.Chrome(service=service)

# driver = webdriver.Chrome("chromedriver.exe")



driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()  # 最大化窗口
driver.implicitly_wait(10)
# # driver.find_element_by_link_text('热点').click()  # 点击热点
# driver.implicitly_wait(10)

title_list = []


def scoll():  # 滚动页面 class="sport-card"
    driver.execute_script("window.scrollTo(0,1000);")
    time.sleep(1)
    from selenium.webdriver.common.by import By
    names = driver.find_elements(by=By.CLASS_NAME, value="container-inner-content")
    for name in names:
        month = name.find_element(by=By.CLASS_NAME, value="odds-left").find_element(by=By.TAG_NAME,value="span").get_attribute("innerText")
        elements = name.find_elements(by=By.TAG_NAME, value="odds-card-sport")
        print(f'爬取日期={month}')
        for element in elements:
            header_element = element.find_element(by=By.CLASS_NAME,value="sport-card-header")
            data_time = header_element.find_element(by=By.CLASS_NAME,value="sport-card-left").find_element(by=By.TAG_NAME,value="span").get_attribute("innerText")
            data_score = header_element.find_element(by=By.CLASS_NAME, value="sport-card-right").find_element(
                by=By.TAG_NAME, value="a").get_attribute("innerHTML")

            team_elements = element.find_element(by=By.CLASS_NAME,value="sport-card-content").find_element(by=By.CLASS_NAME, value="sport-card-left").find_elements(
                by=By.TAG_NAME, value="a")

            team1 = team_elements[0].get_attribute("innerHTML")
            team2 = team_elements[0].get_attribute("innerHTML")
            print(f'比赛日期={data_time},data_score={data_score},teamA={team1},teamB={team2}')




# 运行scoll函数
scoll()

