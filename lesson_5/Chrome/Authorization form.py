from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get("http://the-internet.herokuapp.com/login")

username = chrome.find_element(
    By.CSS_SELECTOR, ("#username")).send_keys("tomsmith")
password = chrome.find_element(
    By.CSS_SELECTOR, ("#password")).send_keys("SuperSecretPassword!")
Login = chrome.find_element(
    By.CSS_SELECTOR, ('button[type="submit"]')).click()

chrome.quit()
