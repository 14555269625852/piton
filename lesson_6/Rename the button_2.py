from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Firefox()
chrome.get("http://uitestingplayground.com/textinput")

specify_the_text = chrome.find_element(
    By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")
click_button = chrome.find_element(
    By.CSS_SELECTOR, ('button[class="btn btn-primary"]')).click()
get_the_text = chrome.find_element(
    By.CSS_SELECTOR, "#updatingButton").text

print(get_the_text)

chrome.quit()
