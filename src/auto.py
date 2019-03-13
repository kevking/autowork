# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time


class AUTO:
    def __init__(self):
        self.driver = webdriver.Chrome('../driver/chromedriver.exe') # 登录目标网页

    def login(self):
        self.driver.get("http://rpt.mis.bcs:8080/rpt-web/index")
        time.sleep(1)
        # 提交表单登录
        we_accout = self.driver.find_element_by_css_selector('#loginTable > tbody > tr:nth-child(2) > td:nth-child(2) > div > input')
        we_accout.clear()
        we_accout.send_keys("5669")

        we_accout = self.driver.find_element_by_css_selector('#loginTable > tbody > tr:nth-child(3) > td:nth-child(2) > div > input')
        we_accout.clear()
        we_accout.send_keys("abcd@1234")

        # 点击提交
        self.driver.find_element_by_css_selector('#loginTable > tbody > tr:nth-child(4) > td:nth-child(2) > a').click()
        time.sleep(2)

    def click(self, selector):
        element = self.driver.find_element_by_css_selector(selector)
        element.click()

    def send_key(self, value):
        self.driver.find_element_by_id("kw").send_keys(value)

    def bussiness(self):
        #点击储蓄存款日报表
        self.driver.switch_to.frame('contentFrame')
        ifra = auto.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div/iframe')
        self.driver.switch_to.frame(ifra)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/ul/li[2]/p/a').click()
        time.sleep(1)
        #切换到报表界面
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('reportWin')
        #选择个人保本理财
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/form/div/ul/li[7]/ul/li[2]/div/div/div[3]/div').click()
        self.driver.find_element_by_xpath('/html/body/div[9]/div[1]/table/tbody/tr[4]/td').click()
        #点击查询
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/div/div').click()
        time.sleep(1)
        #点击下载
        self.driver.switch_to.frame('report')
        self.driver.find_element_by_xpath('/html/body/div[1]/ul/li[1]/ul/li[2]/a/span').click()

        #选择个人结构性存款
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('reportWin')
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/form/div/ul/li[7]/ul/li[2]/div/div/div[3]/div').click()
        self.driver.find_element_by_xpath('/html/body/div[9]/div[1]/table/tbody/tr[5]/td').click()
        #点击查询
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/div').click()
        time.sleep(2)
        #点击下载
        self.driver.switch_to.frame('report')
        self.driver.find_element_by_xpath('/html/body/div[1]/ul/li[1]/ul/li[2]/a/span').click()

        #点击分支行经营情况总览表
        self.driver.get("http://rpt.mis.bcs:8080/rpt-web/index")
        self.driver.switch_to.frame('contentFrame')
        ifra = auto.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div/iframe')
        self.driver.switch_to.frame(ifra)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/ul/li[3]/p/a').click()
        time.sleep(1)
        #切换到报表界面
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('reportWin')
        #点击查询
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/div/div').click()
        time.sleep(1)
        #点击下载
        self.driver.switch_to.frame('report')
        self.driver.find_element_by_xpath('/html/body/div[1]/ul/li[1]/ul/li[2]/a/span').click()

        #点击存贷款日报表
        self.driver.get("http://rpt.mis.bcs:8080/rpt-web/index")
        self.driver.switch_to.frame('contentFrame')
        ifra = auto.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div/iframe')
        self.driver.switch_to.frame(ifra)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/ul/li[4]/p/a').click()
        time.sleep(1)
        #切换到报表界面
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('reportWin')
        #点击查询
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/div/div').click()
        time.sleep(1)
        #点击下载
        self.driver.switch_to.frame('report')

        #点击存款日报表
        self.driver.get("http://rpt.mis.bcs:8080/rpt-web/index")
        self.driver.switch_to.frame('contentFrame')
        ifra = auto.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[4]/div/iframe')
        self.driver.switch_to.frame(ifra)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/ul/li[4]/p/a').click()
        time.sleep(1)
        #切换到报表界面
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('reportWin')
        #选择保本理财
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('reportWin')
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/form/div/ul/li[6]/ul/li[2]/div/div/div[3]/div').click()
        self.driver.find_element_by_xpath('/html/body/div[8]/div[1]/table/tbody/tr[8]/td').click()
        #点击查询
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/div/div').click()
        time.sleep(1)
        #点击下载
        self.driver.switch_to.frame('report')


if __name__ == '__main__':
    auto = AUTO()
    auto.login()
    auto.bussiness()

