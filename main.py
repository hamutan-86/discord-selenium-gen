from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from bs4 import BeautifulSoup
from random_username.generate import generate_username
from selenium.webdriver.common.keys import Keys
import urllib.parse
import requests
import secrets
import random
import time

def index():
  options = Options()
  driver = webdriver.Chrome(options=options)
  driver.get(f"https://www.onetime-mail.com/?q=make2")
  inputs = driver.find_elements(By.TAG_NAME, "input")
  for input in inputs:
    if "mymail" in input.get_attribute("id"):
      email = input.get_attribute("value")
      driver.get("https://discord.com/register")
      time.sleep(2)
      # email
      element = driver.find_element(By.CSS_SELECTOR, "#uid_7")
      element.click()
      action = webdriver.ActionChains(driver)
      action.send_keys(email).perform()
      # global_name
      element = driver.find_element(By.CSS_SELECTOR, "#uid_8")
      element.click()
      action = webdriver.ActionChains(driver)
      action.send_keys(generate_username(1)[0]).perform()
      # username
      element = driver.find_element(By.CSS_SELECTOR, "#uid_9")
      element.click()
      action = webdriver.ActionChains(driver)
      action.send_keys(str(random.randint(100000000000, 999999999999))).perform()
      # password
      element = driver.find_element(By.CSS_SELECTOR, "#uid_10")
      element.click()
      action = webdriver.ActionChains(driver)
      action.send_keys(secrets.token_urlsafe(16)).perform()
      # dob_month
      element = driver.find_element(By.CSS_SELECTOR, "#react-select-2-input")
      element.send_keys(str(random.randint(1
, 12)))
      element.send_keys(Keys.ENTER)
      # dob_day
      element = driver.find_element(By.CSS_SELECTOR, "#react-select-3-input")
      element.send_keys(str(random.randint(1, 30)))
      # dob_year
      element = driver.find_element(By.CSS_SELECTOR, "#react-select-4-input")
      element.send_keys(str(random.randint(1980, 2004)))
      element.send_keys(Keys.ENTER)
      # checkboxes
      chks = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
      for chk in chks:
        chk.click()
      # register_button
      btns = driver.find_elements(By.TAG_NAME, "button")
      for btn in btns:
        if btn.text == "Continue":
          btn.click()
      return

index()
