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
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAnypass():
    def setup_method(self, method):
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_anypass(self):
        self.driver.get("https://store.anypass.jp/resale-list?sort=0")

        while True:
            login = 0

            try:
                name_element = self.driver.find_element(By.CSS_SELECTOR, ".name")
                if "佐々木" in name_element.text:
                    login = 1
            except NoSuchElementException:
                print("ログインします")

            if login == 0:
                self.driver.find_element(By.CSS_SELECTOR, ".pc:nth-child(2)").click()
                self.driver.find_element(By.NAME, "mail").send_keys("33shunshun33@gmail.com")
                self.driver.find_element(By.NAME, "password").send_keys("Banjapoxanypass!")
                self.driver.find_element(By.CSS_SELECTOR, ".button__container__inverted:nth-child(4) > .button__element").click()

            try:
                # WebDriverWaitを使って特定の条件が満たされるまで待つ
                select_element = WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".custom-select:nth-child(1) > .select-selected"))
                )
                select_element.click()

                self.driver.find_element(By.CSS_SELECTOR, ".custom-select:nth-child(1) div:nth-child(1)").click()
                title_element = self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) > .item__details > .title")
                status_element = self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) > .item__category.red")

                if "TAYLOR SWIFT | THE ERAS TOUR" in title_element.text and not ("Being Purchased" in status_element.text):
                    break  # while文を抜ける
            except NoSuchElementException:
                print("所望のチケットではありません、繰り返します")

        self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) > .item__details").click()
        self.driver.find_element(By.CSS_SELECTOR, ".checkmark").click()
        self.driver.find_element(By.CSS_SELECTOR, ".buy__container > div").click()
