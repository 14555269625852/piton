from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from time import sleep

chrome = webdriver.Chrome()
chrome.get("http://the-internet.herokuapp.com/entry_ad")
sleep(3)
try:
    close = chrome.find_element(
        By.CSS_SELECTOR, ("div[class='modal-footer']")).click()
    print("закрыто окно")
except ElementNotInteractableException:
    chrome.quit()
