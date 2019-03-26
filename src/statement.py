#'/html/body/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/div/div' -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import json


class Statement:
    url = "http://rpt.mis.bcs:8080/rpt-web/index"
    config_file = "c://config.json"
    locateUsername = '#loginTable > tbody > tr:nth-child(2) > td:nth-child(2) > div > input'
    locatePasswd = '#loginTable > tbody > tr:nth-child(3) > td:nth-child(2) > div > input'
    locateSubmit = '#loginTable > tbody > tr:nth-child(4) > td:nth-child(2) > a'
    locateMenuIframe = '/html/body/div/div/div[1]/div[3]/div/iframe'
    locateMenu = ['/html/body/div/div[2]/div/div[2]/div/ul/li[0]/p/a',
                  '/html/body/div/div[2]/div/div[2]/div/ul/li[1]/p/a',
                  '/html/body/div/div[2]/div/div[2]/div/ul/li[2]/p/a',
                  '/html/body/div/div[2]/div/div[2]/div/ul/li[3]/p/a',
                  '/html/body/div/div[2]/div/div[2]/div/ul/li[4]/p/a']
    locateChuxuXM = '/html/body/div[2]/div[1]/div/div[2]/form/div/ul/li[7]/ul/li[2]/div/div/div[3]/div'
    locateCunkuanXM = '/html/body/div[2]/div[1]/div/div[2]/form/div/ul/li[6]/ul/li[2]/div/div/div[3]/div'
    #locateChuxuJG = '/html/body/div[2]/div[1]/div/div[2]/form/div/ul/li[2]/ul/li[2]/div/div/div[3]/div'
    locateChuxuItem = ['/html/body/div[9]/div[1]/table/tbody/tr[0]/td',
                       '/html/body/div[9]/div[1]/table/tbody/tr[1]/td',
                       '/html/body/div[9]/div[1]/table/tbody/tr[2]/td',
                       '/html/body/div[9]/div[1]/table/tbody/tr[3]/td',
                       '/html/body/div[9]/div[1]/table/tbody/tr[4]/td',
                       '/html/body/div[9]/div[1]/table/tbody/tr[5]/td']

    locateCunkuanItem = ['/html/body/div[8]/div[1]/table/tbody/tr[0]/td',
                         '/html/body/div[8]/div[1]/table/tbody/tr[1]/td',
                         '/html/body/div[8]/div[1]/table/tbody/tr[2]/td',
                         '/html/body/div[8]/div[1]/table/tbody/tr[3]/td',
                         '/html/body/div[8]/div[1]/table/tbody/tr[4]/td',
                         '/html/body/div[8]/div[1]/table/tbody/tr[5]/td',
                         '/html/body/div[8]/div[1]/table/tbody/tr[6]/td',
                         '/html/body/div[8]/div[1]/table/tbody/tr[7]/td',
                         '/html/body/div[8]/div[1]/table/tbody/tr[8]/td',
                         '/html/body/div[8]/div[1]/table/tbody/tr[9]/td',
                         '/html/body/div[8]/div[1]/table/tbody/tr[10]/td',
                         ]

    locateChaxun = '/html/body/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/div/div'
    locateDownload = '/html/body/div[1]/ul/li[1]/ul/li[2]/a/span'
    # locateChuxuGZ = '/html/body/div[4]/div[1]/table/tbody/tr[3]/td'

    def __init__(self):
        self.driver = webdriver.Chrome('../driver/chromedriver.exe')  # 登录目标网页
        self.driver.maximize_window()

    def login(self):
        self.driver.get(self.url)
        # 提交表单登录
        with open(self.config_file, "r+") as f:
            config = json.load(f)
        account = self.driver.find_element_by_css_selector(self.locateUsername)
        account.clear()
        account.send_keys(config["NO"])
        account = self.driver.find_element_by_css_selector(self.locatePasswd)
        account.clear()
        account.send_keys(config["passwd"])
        # 点击提交
        self.driver.find_element_by_css_selector(self.locateSubmit).click()

    def enter_menu(self, locate):
        self.driver.get(self.url)
        time.sleep(1)
        self.driver.switch_to.frame('contentFrame')
        ifra = self.driver.find_element_by_xpath(self.locateMenuIframe)
        self.driver.switch_to.frame(ifra)
        self.driver.find_element_by_xpath(locate).click()
        time.sleep(1)
        # 切换到报表界面
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('reportWin')

    def select_item(self, locate, item):
        # 切换到报表界面
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('reportWin')
        # 选择个人保本理财
        self.driver.find_element_by_xpath(locate).click()
        self.driver.find_element_by_xpath(item).click()

    def download(self):
        #点击查询
        self.driver.find_element_by_xpath(self.locateChaxun).click()
        time.sleep(1)
        #点击下载
        self.driver.switch_to.frame('report')
        self.driver.find_element_by_xpath(self.locateDownload).click()

    def run(self):
        # 下载储蓄存款日报表-个人保本理财
        self.enter_menu(self.locateMenu[1])
        self.select_item(self.locateChuxuXM, self.locateChuxuItem[4])
        self.download()
        # 下载储蓄存款日报表(1)-个人结构性存款
        self.select_item(self.locateChuxuXM, self.locateChuxuItem[5])
        self.download()
        # 下载储蓄存款日报表(2)-储蓄存款
        self.select_item(self.locateChuxuXM, self.locateChuxuItem[2])
        # self.select_item(self.locateChuxuJG, self.locateChuxuGZ)
        self.download()

        # 下载存贷款日报表
        self.enter_menu(self.locateMenu[3])
        self.download()
        # 下载存款日报表
        self.enter_menu(self.locateMenu[4])
        self.select_item(self.locateCunkuanXM, self.locateCunkuanItem[9])
        self.download()
        # 下载经营情况总览表
        self.enter_menu(self.locateMenu[2])
        self.download()


if __name__ == '__main__':
    auto = Statement()
    auto.login()
    auto.run()

