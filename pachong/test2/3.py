# -*- coding: UTF-8 -*-
# @author: caoyang
# @email: caoyang@163.sufe.edu.cn

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


# 读取存放搜索关键词的文件
# 文件中的每一行只记录一条关键词
# 以'#'开头的行会被自动忽略, 尽量不要出现空行
def load_keywords(filepath: str) -> list:
    with open(filepath, 'r', encoding='utf8') as f:
        keywords = f.read().splitlines()
    return list(filter(lambda x: not x.startswith('#'), keywords))


class Xuebalib(object):

    def __init__(self,
                 keywords: list,
                 username: str,
                 password: str,
                 host: str,
                 extension_path: str = None,
                 mode: str = 'expert') -> None:
        self.keywords = keywords[:]
        self.username = username
        self.password = password
        self.host = host
        self.extension_path = extension_path  # 与2020年的情况出现重大区别, 2021年学霸图书馆通道进入需要安装插件, 需下载crx格式的插件并记录路径
        self.mode = mode.strip().lower()
        assert self.mode in ['quick', 'expert'], f'Unknown mode: {self.mode}'

        self.max_trial_time = 8

    @staticmethod
    def get_detailurl(soup: BeautifulSoup) -> list:
        """
        获取索结果页面上所有论文详情页面的链接:
        :param soup: 经过BeautifulSoup解析后的页面源代码;
        """
        detaillinks = soup.find_all('a', class_='detaillink')
        detailurls = []
        for detaillink in detaillinks:
            detailurl = detaillink.attrs['href']
            detailurls.append(detailurl)
        return detailurls

    @staticmethod
    def get_author_and_email(soup: BeautifulSoup, ignore: bool = False) -> list:
        """获取论文详情页面上的作者及对应的邮箱
        :param soup				: 经过BeautifulSoup解析后的页面源代码;
        :param ignore			: 是否忽略那些没有邮箱的作者, 默认不忽略;

        :return author_and_email: 作者和邮箱构成的二元组列表;
        """
        author_and_email = []
        if ignore:
            emaillinks = soup.find_all('a', class_='emaillink')
            for emaillink in emaillinks:
                email = emaillink.attrs['href']
                authorlink = emaillink.find_previous_sibling('a', class_='authorSearchLink')
                author = str(authorlink.string)
                author_and_email.append((author, email))
        else:
            ul = soup.find('ul', class_='abs_authors')
            if ul is not None:
                for li in ul.find_all('li'):
                    authorlink = li.find('a', class_='authorSearchLink')
                    emaillink = li.find('a', class_='emaillink')
                    author = str(authorlink.string)
                    email = None if emaillink is None else emaillink.attrs['href']
                    author_and_email.append((author, email))
        return author_and_email

    def run(self):
        # 初始化浏览器驱动
        print('Initiate driver ...')
        if self.extension_path is not None:
            chrome_options = webdriver.ChromeOptions()  # 初始化Chrome选项
            chrome_options.add_extension(self.extension_path)  # 安装学霸图书馆通道插件
            chrome_options.add_argument(r'user-data-dir=C:\Users\lenovo\AppData\Local\Google\Chrome\User Data')
            chrome_options.add_experimental_option('useAutomationExtension', False)
            driver = webdriver.Chrome(chrome_options=chrome_options)  # 配置Chrome选项
        else:  # 通常这种情况目前是不可行的, 不过以后可能又不需要插件了, 即可恢复为默认的火狐浏览器驱动更加稳定
            driver = webdriver.Firefox()
        driver.set_page_load_timeout(15)  # 设置最长加载时间, 否则会卡死在论文详情页面
        driver.maximize_window()  # 最大化窗口: 2021年新改变, 如果不最大化窗口, 搜索页面布置将会发生变化, 无法转为expert模式
        print('  - Complete !')

        # 登录学霸图书馆
        print('Login ...')
        driver.get('http://www.xuebalib.com')
        print('  - Waiting for textinput ...')
        WebDriverWait(driver, 30).until(
            lambda driver: driver.find_element_by_xpath('//input[@name="username"]').is_displayed())
        print('    + OK !')
        print('  - Input username and password ...')
        driver.find_element_by_xpath('//input[@name="username"]').send_keys(self.username)
        driver.find_element_by_xpath('//input[@name="password"]').send_keys(self.password)
        driver.find_element_by_xpath('//input[@value="登陆"]').click()
        print('    + OK !')
        time.sleep(3)
        print('  - Complete !')

        # 取得通道访问权限: 2021年使用BUAA(北京航空航天大学)通道
        print('Get through Passageway ... (It is extremely slow and may be failed for several times)')
        driver.get('http://www.xuebalib.com/db.php/EI')
        print('  - Waiting for Passageway link ...')
        WebDriverWait(driver, 30).until(
            lambda driver: driver.find_element_by_xpath('//a[contains(text(), "BUAA")]').is_displayed())
        print('    + OK !')
        print('  - Enter Passageway ...')
        driver.find_element_by_xpath('//a[contains(text(),"BUAA")]').click()
        print('    + OK !')
        print('  - Switch to new window ...')
        windows = driver.window_handles  # 初始化窗口句柄
        print(f'    + Totally {len(windows)} windows !')
        driver.switch_to.window(windows[1])  # 转到新窗口
        print('    + OK !')

        print('  - Access to Engineering Village ... (It is the most difficult step and always failed)')
        WebDriverWait(driver, 60).until(lambda driver: driver.find_element_by_xpath(
            '//a[@href="https://www-engineeringvillage-com.e1.buaa.edu.cn"]').is_displayed())

        # 开始进行搜索
        count = 0
        for index, keyword in enumerate(self.keywords):

            flag = 1
            while flag <= self.max_trial_time:
                try:
                    print(f'    + No.{flag} Trial ...')
                    driver.get(
                        'http://www.engineeringvillage.com')  # 20211017更新: 之前为什么这个链接行不通, 因为没有把User Data加进来, 导致一直落在Welcome界面无法权限登录, 今早试出来要chrome_options.add_argument(r'user-data-dir=C:\Users\lenovo\AppData\Local\Google\Chrome\User Data'), 走这个通道更稳定
                    # driver.get('https://www-engineeringvillage-com-443.e1.buaa.edu.cn/search/quick.url')
                    # driver.find_element_by_xpath('//a[@href="https://www-engineeringvillage-com.e1.buaa.edu.cn"]').click()
                    print('    + Waiting for search textinput ...')
                    WebDriverWait(driver, 60).until(
                        lambda driver: driver.find_element_by_xpath('//input[@class="search-word"]').is_displayed())
                    print('    + OK !')
                    break
                except Exception as e:
                    flag += 1
                    print(f'      * Fail: {e}')
                    continue
            print('  - Complete !')

            # 再次确认已经进入Engineering Village
            print('Waiting for search textinput again ...')
            WebDriverWait(driver, 60).until(
                lambda driver: driver.find_element_by_xpath('//input[@class="search-word"]').is_displayed())
            print('  - Complete !')

            if self.mode == 'expert':  # export模式下转为专家搜索
                print('Switch to expert mode ...')
                driver.find_element_by_xpath('//span[@class="button-link-text" and contains(text(),"Search")]').click()
                time.sleep(1)
                driver.find_element_by_xpath('//span[@class="button-link-text" and contains(text(),"Expert")]').click()
                print('  - Complete !')

            print(f'Search keyword: {keyword}')
            with open(f'keyword_{index}.txt', 'w', encoding='utf8') as f:
                pass

            # 重置搜索框
            print('  - Reset textinput ...')
            xpath = '//a[@id="reset-form-link-quick"]' if self.mode == 'quick' else '//a[@id="reset-form-link-expert"]'
            driver.find_element_by_xpath(xpath).click()
            time.sleep(2)
            print('    + OK !')

            # 输入关键词
            print('  - Input keyword ...')
            xpath = '//input[@class="search-word"]' if self.mode == 'quick' else '//textarea[@class="search-word text-area-lg"]'
            driver.find_element_by_xpath(xpath).send_keys(keyword)
            time.sleep(2)
            print('    + OK !')

            # 点击搜索
            print('  - Click search engine ...')
            xpath = '//a[@id="searchBtn"]' if self.mode == 'quick' else '//a[@id="expertSearchBtn"]'
            driver.find_element_by_xpath(xpath).click()
            print('    + OK !')

            # 等待搜索结果
            print('  - Waiting for search results ...')
            WebDriverWait(driver, 60).until(
                lambda driver: driver.find_element_by_xpath('//a[@class="detaillink"]').is_displayed())
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            h2 = soup.find('h2', id='results-count')
            for child in h2.children:
                results_count = int(str(child).strip())
                break
            print(f'    + Totally {results_count} results !')
            current_url = driver.current_url  # 记录当前URL, 便于再次回到该页面
            time.sleep(3)
            print('    + OK !')

            # *** 试图调整下拉框每页显示数量100, 这样可以少翻几页, 但是不知为何无法使用Select方法
            # driver.find_element_by_xpath('//span[@class='select2-selection__arrow']').click()
            # time.sleep(2)
            # select_el = Select(driver.find_element_by_xpath('//select[@id='results-per-page-select']'))
            # select_el.select_by_visible_text('100')

            current_index = 1  # 记录搜索结果的序号
            page_number = 0  # 记录分页值
            while True:
                page_number += 1  # 遍历每一页搜索结果
                print(f'  - Page {page_number} ...')
                html = driver.page_source
                soup = BeautifulSoup(html, 'lxml')
                detailurls = Xuebalib.get_detailurl(soup)
                for detailurl in detailurls:
                    count += 1
                    print(f'    + Processing No.{count} paper ...')
                    try:  # 可能会失败: 原因是来自配置driver.set_page_load_timeout(10), 但是不配置页面最长加载时间, 其他地方也可能会报错
                        driver.get(self.host + detailurl)
                        WebDriverWait(driver, 30).until(
                            lambda driver: driver.find_element_by_xpath('//ul[@class="abs_authors"]').is_displayed())
                    except:  # 虽然加载不完全, 不过无所谓反正需要的信息大概率都已经加载出来了
                        print('    + Load incompletely ! (Do not care about this)')
                    # 解析作者及邮箱
                    html = driver.page_source
                    soup = BeautifulSoup(html, 'lxml')
                    author_email_pairs = Xuebalib.get_author_and_email(soup, ignore=False)
                    # 将作者及邮箱写入文件
                    print('    + Write to file ...')
                    for author, email in author_email_pairs:
                        with open(f'keyword_{index}.txt', 'a', encoding='utf8') as f:
                            f.write(f'{author}\t{email}\n')
                    print('    + OK !')

                # 回到搜索结果页面并点击下一页: 这种方法不太稳定
                # driver.get(current_url)
                # try:													 # 如果已经到最后一页, 就会发现没有不存在下一页按钮了
                # WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath('//a[@id='next-page-top']').is_displayed())
                # except:												 # 此时退出循环
                # break
                # driver.find_element_by_xpath('//a[@id='next-page-top']').click()
                # WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath('//a[@class='detaillink']').is_displayed())
                # current_url = driver.current_url

                # 所以想了个好办法, 可以直接通过改变查询字符串转到下一页
                current_index += 25  # 默认每页25个, 因为上面下拉框改成100个的逻辑总是失败, 所以以后分页数量变了得自己记得改
                if current_index > results_count:  # 一旦超过之前记录的搜索结果数量就表明该关键词已经爬取完毕
                    break
                index1 = current_url.find('COUNT=')
                index2 = current_url.find('&', index1)
                next_url = current_url[: index1 + 6] + str(current_index) + current_url[index2:]
                while True:
                    try:
                        print(f'  - Switch to next page (next page is {page_number + 1})...')
                        driver.get(next_url)
                        print('    + Waiting for search results ...')
                        WebDriverWait(driver, 30).until(
                            lambda driver: driver.find_element_by_xpath('//a[@class="detaillink"]').is_displayed())
                        print('    + OK !')
                        break
                    except Exception as e:
                        print(f'    + Fail: {e} ...')
                        continue


if __name__ == '__main__':
    keywords = load_keywords('kw.txt')
    print(keywords)
    username = ''  # 学霸图书馆用户名
    password = ''  # 学霸图书馆密码
    # host = 'https://www-engineeringvillage-com-443.e1.buaa.edu.cn'		 # 学霸图书馆用于访问Engineering Village的大学主机URL: 2020年使用的是沈阳工业大学的主机(http://202.199.103.219), 2021年最新使用的是北京航空航天大学的主机
    host = 'http://www.engineeringvillage.com'  # 20211017更新: 可以跳过通道直接访问
    extension_path = 'D:/xuebalib.crx'  # 学霸图书馆用于通道访问的插件: 由于浏览器驱动默认不会带插件, 即便浏览器上已经安装了自动启动的插件, 在驱动时也不会启用插件, 因此需要每次加载插件
    mode = 'expert'  # 建议使用export模式而非默认的quick模式, 因为前者相对不容易出错

    xuebalib = Xuebalib(keywords=keywords,
                        username=username,
                        password=password,
                        host=host,
                        extension_path=extension_path,
                        mode=mode)
    xuebalib.run()
