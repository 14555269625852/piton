from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
chrome.get("http://uitestingplayground.com/classattr")

sleep(5)
for x in range(1, 4):
    blue_button = chrome.find_element(
        By.CSS_SELECTOR, ("button[class='btn btn-primary']")).click()
    alert = chrome.switch_to.alert
    alert.accept()
print(x)

chrome.quit()
