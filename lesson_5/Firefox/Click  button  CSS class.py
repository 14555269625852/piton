from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

firefox = webdriver.Firefox()
firefox.get("http://uitestingplayground.com/classattr")

sleep(2)
for x in range(1, 4):
    blue_button = firefox.find_element(
        By.CSS_SELECTOR, ('button[class="btn btn-primary"]')).click()
    alert = firefox.switch_to.alert
    alert.accept()
print(x)

firefox.quit()
