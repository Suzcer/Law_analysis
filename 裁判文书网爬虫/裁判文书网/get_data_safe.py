"""
download documents

        稳定版本，但仍有问题：
        1.登录界面弹出验证码
        2.time.sleep()消耗过多时间


"""
import base64
import os
import time
import random

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import json
from selenium.webdriver.common.action_chains import ActionChains


class GetData:
    """
    获取数据
    """

    def random_sleep(self, mu=1, sigma=0.4):
        '''正态分布随机睡眠
        :param mu: 平均值
        :param sigma: 标准差，决定波动范围
        '''
        secs = random.normalvariate(mu, sigma)
        if secs <= 0:
            secs = mu  # 太小则重置为平均值
        time.sleep(secs)

    def __init__(self):
        self.url = 'https://wenshu.court.gov.cn/website/wenshu/181029CR4M5A62CH/index.html?#'

        #这是刑事案件的网址

        options = webdriver.ChromeOptions()
        options.add_argument('--log-level=3')
        #修改windows.navigator.webdriver，防机器人识别机制，selenium自动登陆判别机制
        options.add_experimental_option(
            'excludeSwitches', ['enable-logging', 'enable-automation'])
        prefs = {
            'profile.default_content_settings.popups': 0,   #防止保存弹窗
            'download.default_directory': 'text\\',         #设置默认下载路径
            "profile.default_content_setting_values.automatic_downloads": 1 #允许多文件下载
        }
        options.add_experimental_option('prefs', prefs)
        self.timeout = 30
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\Dudu\Downloads\Compressed\chromedriver_win32\chromedriver.exe',
            service_log_path=os.devnull,
            options=options)
        # self.driver = webdriver.Edge(
        #     # executable_path='C:\\Program Files (x86)\\Microsoft\Edge\\Application\\msedge.exe',
        #     executable_path='C:\\Users\\Dudu\\Downloads\\Compressed\\edgedriver_win64\\msedgedriver.exe',
        #     service_log_path=os.devnull,
        #     # options=options
        # )

        self.driver.maximize_window()
        self.driver.set_page_load_timeout(self.timeout)
        self.driver.get(self.url)
        self.read_cookies()
        self.driver.refresh()
        self.driver.refresh()

        # cookies = self.driver.get_cookies()
        # with open("cookies.txt", "w") as fp:
        #     json.dump(cookies, fp)


    def read_cookies(self):
        with open("cookies.txt", "r") as fp:
            cookies = json.load(fp)
            for cookie in cookies:
                # cookie.pop('domain')  # 如果报domain无效的错误
                self.driver.add_cookie(cookie)


    def login(self):
        """
        login
        """

        # time.sleep(2)
        # self.driver.find_element_by_id('loginLi').click()
        # time.sleep(2)
        # #登录
        # iframe = self.driver.find_element_by_id('contentIframe')
        # WebDriverWait(self.driver, self.timeout).until(
        #     EC.frame_to_be_available_and_switch_to_it(iframe))
        # self.driver.switch_to.frame(iframe)
        # username_input = self.driver.find_element_by_name('username')
        # username_input.send_keys('18924995651')
        # time.sleep(3)
        # passwd_input = self.driver.find_element_by_name('password')
        # passwd_input.send_keys('13680216163Qq@')
        # time.sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="root"]/div/form/div[3]/span').click()
        time.sleep(30)



    def get_data(self):
        """
        download
        """
        self.login()

        self.random_sleep()

        #这一步点击了"高级检索"的搜索框
        self.driver.find_element_by_xpath('//*[@id="_view_1540966814000"]/div/div[1]/div').click()
        # link=self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/a[8]")
        # ActionChains(self.driver).move_to_element(link).perform()         #备用方案，可能可行

        #找到“全文检索”
        self.random_sleep()
        search_input=self.driver.find_element_by_xpath('//*[@id="_view_1540966814000"]/div/div[3]/div[1]/div[1]/div/input')
        search_input.click()
        search_input.send_keys('刑事裁定书')
        self.random_sleep()
        self.driver.find_element_by_xpath('//*[@id="_view_1540966814000"]/div/div[3]/div[1]/div[1]/div/div/span').click()
        self.random_sleep()
        self.driver.find_element_by_xpath('//*[@id="_view_1540966814000"]/div/div[3]/div[1]/div[1]/div/ul/li[2]').click()


        #找到“文书类型”并选择“裁定书”
        self.random_sleep()
        self.driver.find_element_by_xpath('//*[@id="_view_1540966814000"]/div/div[3]/div[1]/div[9]/div/div/div/span').click()
        self.random_sleep()
        self.driver.find_element_by_xpath('//*[@id="_view_1540966814000"]/div/div[3]/div[1]/div[9]/div/div/ul/li[4]').click()


        #找到“裁判日期”
        self.random_sleep()
        search_input=self.driver.find_element_by_xpath('//*[@id="cprqStart"]')
        self.random_sleep()
        search_input.send_keys('2019-1-10')
        self.random_sleep()
        search_input=self.driver.find_element_by_xpath('//*[@id="cprqEnd"]')
        self.random_sleep()
        search_input.send_keys('2019-3-10')
        self.random_sleep()

        #找到“检索”并且点击
        self.driver.find_element_by_xpath('//*[@id="_view_1540966814000"]/div/div[3]/div[2]/a[1]').click()
        self.random_sleep()
        self.driver.refresh()
        self.random_sleep()
        #WebDriverWait(self.driver,30).until()


        #快速搜索栏
        # search_input = self.driver.find_element_by_xpath('//*[@id="_view_1540966814000"]/div/div[1]/div[2]/input')
        # #这两行就是找到快速搜索栏的
        # # WebDriverWait(self.driver, self.timeout).until(
        # #     EC.visibility_of_element_located(search_input))
        # search_input.click()
        # search_input.send_keys('刑事裁定书')
        # self.driver.find_element_by_xpath('//*[@id="_view_1540966814000"]/div/div[1]/div[3]').click()
        # time.sleep(6)

        # 每页15结果
        #selector = Select(self.driver.find_element_by_xpath('//*[@id="_view_1545184311000"]/div[8]/div/select'))
        element = WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_xpath(
                '//*[@id="_view_1545184311000"]/div[8]/div/select'))
        selector=Select(element)
        selector.select_by_visible_text('15')

        page = 1
        while page < 20:
            self.random_sleep()
            # 全选
            self.driver.find_element_by_id('AllSelect').send_keys(Keys.SPACE)
            self.random_sleep()
            # 全部下载 按钮
            self.driver.find_element_by_xpath('//*[@id="_view_1545184311000"]/div[2]/div[4]/a[3]').click()
            self.random_sleep()
            # 下一页
            # self.driver.find_element_by_xpath(
            #     '//*[@id="_view_1545184311000"]/div[8]/a[8]').click()
            self.driver.find_element_by_partial_link_text('下一页').click()
            page += 1

        self.random_sleep()
        self.driver.quit()


if __name__ == '__main__':
    GET_DATA = GetData()
    GET_DATA.get_data()
