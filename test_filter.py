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

class TestFilter():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_filter(self):
    self.driver.get("https://www.google.com/search?q=anypass+store&rlz=1C5CHFA_enJP948JP949&oq=any&gs_lcrp=EgZjaHJvbWUqDggAEEUYJxg7GIAEGIoFMg4IABBFGCcYOxiABBiKBTIGCAEQRRhAMgYIAhBFGDkyDQgDEAAYgwEYsQMYgAQyCggEEC4YsQMYgAQyBggFEEUYPDIGCAYQRRg8MgYIBxBFGDzSAQgyMTcxajBqNKgCALACAA&sourceid=chrome&ie=UTF-8")
    self.driver.set_window_size(1024, 640)
    self.driver.find_element(By.CSS_SELECTOR, ".eKjLze .LC20lb").click()
    self.driver.find_element(By.CSS_SELECTOR, ".checkmark").click()
    self.driver.find_element(By.CSS_SELECTOR, ".button__container__inverted > .button__element").click()
  
