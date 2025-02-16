# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest():
    def setup_method(self, method):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-extensions')
        options.add_argument('--proxy-server="direct://"')
        options.add_argument('--proxy-bypass-list=*')
        options.add_argument('--start-maximized')
        driber_path = "/chromedriver-mac-arm64/chromedriver"
        self.driver = webdriver.Chrome(executable_path=driber_path, options=options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test(self):
        self.driver.get("https://reserve.tokyodisneyresort.jp/")
        self.wait()
        self.driver.find_element(By.XPATH, '//*[@id="header"]/div/ul[2]/li/a/img').click()
        self.wait()
        LoginId = self.driver.find_element(By.XPATH, '//*[@id="_userId"]')
        LoginId.send_keys("<自分のディズニーログインアカウント名>")
        password = self.driver.find_element(By.XPATH, '//*[@id="_password"]')
        password.send_keys("<自分のディズニーログインパスワード>")
        self.driver.find_element(By.XPATH, '//*[@id="_loginConection"]/form/p/a/img').click()
        self.wait()
        self.driver.find_element(By.XPATH, '//*[@id="header"]/div/ul[3]/li[2]/a/img').click()
        self.wait()
        self.driver.find_element(By.XPATH, '//*[@id="dayTable"]/tbody/tr[1]/td/table/tbody/tr/td[2]/a').click()
        self.wait()
        self.driver.find_element(By.XPATH, '//*[@id="searchCalendar"]/div/div/ul/button[2]').click()

        # ここから先のコードを追加してください

    def wait(self):
        self.driver.implicitly_wait(20)
        WebDriverWait(self.driver, 2000).until(expected_conditions.invisibility_of_element_located((By.ID, 'loading_modal0overlay')))
        time.sleep(5)
