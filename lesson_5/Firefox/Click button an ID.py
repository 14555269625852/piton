from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

firefox = webdriver.Firefox()
firefox.get("http://uitestingplayground.com/dynamicid")
sleep(2)
for x in range(1, 4):
    click_button = firefox.find_element(
        By.CSS_SELECTOR, ('button[class="btn btn-primary"]')).click()
    sleep(2)
print("нажать: ", x)

firefox.quit()
