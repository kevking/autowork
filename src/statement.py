#'/html/body/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/div/div' -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import json


class Statement:
    url = "http://www.ejxjy.com/login.html"
    config_file = "d://config.json"
    locateUsername = '/html/body/div[4]/div[1]/div[2]/form/ul/li[1]/input'
    locatePasswd = '/html/body/div[4]/div[1]/div[2]/form/ul/li[2]/input'
    locateSubmit = '//*[@id="loginForm"]/ul/li[4]/input'
    locateEsc =  '//*[@id="loaded"]/div[1]/a'
    # 重新开课后请改回来
    # locateWeixuexi = '//*[@id="a2"]'
    locateWeixuexi = '//*[@id="a3"]'
    # 重新开课后请改回来
    # locateJxxx = '//*[@id="con_a_2"]/ul/li[1]/div[2]/a'
    locateJxxx = '//*[@id="con_a_3"]/ul/li[1]/div[2]/a'
    locateSave = '/html/body/div/div[1]/div[2]/ul/li[1]/a'
    locateQueding = '/html/body/div[2]/div[4]/table/tbody/tr[2]/td[2]/div/div[2]/div/div[2]/button'
    locateDuration = '/html/body/div/div[3]/div/div[1]/div[3]/div[7]/div[3]/div[1]/span[3]'

    def __init__(self):
        self.driver = webdriver.Chrome(r'D:/Desktop/autowork-master/driver/chromedriver.exe')  # 登录目标网页
        self.driver.maximize_window()

    def login(self):
        self.driver.get(self.url)
        # 提交表单登录
        with open(self.config_file, "r+") as f:
            config = json.load(f)
        user_name = config["username"]
        pass_word = config["passwd"]
        print(user_name)
        print(pass_word)
        self.driver.find_element_by_xpath(self.locateUsername).send_keys(user_name)
        self.driver.find_element_by_xpath(self.locatePasswd).send_keys(pass_word)
        # 点击提交
        self.driver.find_element_by_xpath(self.locateSubmit).click()

    def run(self):
        self.driver.implicitly_wait(5)
        #关闭提示窗口
        self.driver.find_element_by_xpath(self.locateEsc).click()
        #点击未学习
        self.driver.find_element_by_xpath(self.locateWeixuexi).click()
        #点击继续学习
        self.driver.find_element_by_xpath(self.locateJxxx).click()
        time.sleep(2)

    def isExist(self, element):
        flag = True
        browser = self.driver
        try:
            browser.find_element_by_xpath(element)
            return flag
        except:
            flag = False
            return flag

    def close(self):
        #获取窗口句柄
        windows = self.driver.window_handles
        #切换到新窗口
        self.driver.switch_to.window(windows[1])
        # 获取到视频时长，直接睡指定时间
        shijian = self.driver.find_element_by_xpath(self.locateDuration).text.split(':',1)
        print(int(shijian[0])*60 + int(shijian[1]))
        time.sleep(int(shijian[0])*60 + int(shijian[1]) + 10)
        #判断是否弹出完成提示
        if self.isExist(self.locateQueding):
            self.driver.find_element_by_xpath(self.locateQueding).click()
        # 保存
        self.driver.find_element_by_xpath(self.locateSave).click()
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(windows[0])
        self.driver.refresh()
        time.sleep(5)
        return True







if __name__ == '__main__':
    auto = Statement()
    auto.login()
    auto.run()
    while auto.close():
        auto.run()
