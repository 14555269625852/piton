from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

firefox = webdriver.Firefox()
firefox.get("http://the-internet.herokuapp.com/inputs")

enter_number = firefox.find_element(
    By.CSS_SELECTOR, ('input[type="number"]')).send_keys("1000")
sleep(1)
clear_number = firefox.find_element(
    By.CSS_SELECTOR, ('input[type="number"]')).clear()
sleep(1)
new_number = firefox.find_element(
    By.CSS_SELECTOR, ('input[type="number"]')).send_keys("999")
sleep(1)
firefox.quit()
