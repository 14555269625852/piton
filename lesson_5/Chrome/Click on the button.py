from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")

for x in range(1, 6):
    click_on_button = chrome.find_element(
        By.CSS_SELECTOR, ("[onclick='addElement()']")).click()
    chrome_delete_buttons = chrome.find_elements(
        By.XPATH, "//button[@onclick='deleteElement()']")
print(f"Размер спика кнопок Delete in Chrome:{len(chrome_delete_buttons)}")

chrome.quit()
