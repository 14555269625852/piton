from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
chrome.get("http://uitestingplayground.com/dynamicid")
sleep(5)
for x in range(1, 4):
    click_button = chrome.find_element(
        By.CSS_SELECTOR, ('button[class="btn btn-primary"]')).click()
    sleep(5)
print("нажать: ", x)

chrome.quit()
