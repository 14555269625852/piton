from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

firefox = webdriver.Firefox()
firefox.get("http://uitestingplayground.com/classattr")

sleep(5)
for x in range(1, 4):
    try:
        blue_button = firefox.find_element(
            By.CSS_SELECTOR, ("button[class='btn btn-primary']")).click()
        alert = firefox.switch_to.alert
        alert.accept()
    except NoSuchElementException:
        print(x)

firefox.quit()
