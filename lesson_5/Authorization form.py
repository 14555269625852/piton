from selenium import webdriver
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()
firefox.get("http://the-internet.herokuapp.com/login")

username = firefox.find_element(
    By.CSS_SELECTOR, ("#username")).send_keys("tomsmith")
password = firefox.find_element(
    By.CSS_SELECTOR, ("#password")).send_keys("SuperSecretPassword!")
Login = firefox.find_element(
    By.CSS_SELECTOR, ('button[type="submit"]')).click()

firefox.quit()
