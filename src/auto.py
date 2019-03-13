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
        time.sleep(9)

    def click(self, selector):
        element = self.driver.find_element_by_css_selector(selector)
        element.click()

    def send_key(self, value):
        self.driver.find_element_by_id("kw").send_keys(value)

    def bussiness(self):
        # 储蓄存款
        self.driver.find_element_by_xpath('//*[@id="hisrpt_con"]/ul/li[2]/p/a').click()
        self.driver.find_element_by_css_selector('#temps\7c 6 > div > div > div:nth-child(4) > div').click()
        self.driver.find_element_by_css_selector('body > div:nth-child(9) > div.l-box-select-inner > table > tbody > tr:nth-child(4) > td').click()
        #查询
        self.driver.find_element_by_css_selector('#searchbtn').click()
        time.sleep(3)
        #下载
        #TODO 检测是否出现了数据
        self.driver.find_element_by_css_selector('body > div.btnBar > ul > li.toggleBg.borderRight > ul > li:nth-child(2) > a').click()
        time.sleep(3)
        self.driver.find_element_by_css_selector('body > div:nth-child(9) > div.l-box-select-inner > table > tbody > tr:nth-child(5) > td').click()
        #查询
        self.driver.find_element_by_css_selector('#searchbtn').click()
        time.sleep(3)
        #下载
        #TODO 检测是否出现了数据
        self.click('body > div.btnBar > ul > li.toggleBg.borderRight > ul > li:nth-child(2) > a')
        time.sleep(3)
        self.send_key(Keys.ESCAPE)
        self.send_key(Keys.ESCAPE)
        #经营情况总览表
        self.click('#hisrpt_con > ul > li:nth-child(3) > p > a')
        self.click('#searchbtn')
        time.sleep(3)
        #下载
        #TODO 检测是否出现了数据
        self.click('body > div.btnBar > ul > li.toggleBg.borderRight > ul > li:nth-child(2) > a')
        time.sleep(3)
        self.send_key(Keys.ESCAPE)
        self.send_key(Keys.ESCAPE)

if __name__ == '__main__':
    auto = AUTO()
    auto.login()
    #auto.bussiness()
    auto.driver.find_element_by_xpath('//*[@id="hisrpt_con"]/ul/li[2]/p/a').click()


