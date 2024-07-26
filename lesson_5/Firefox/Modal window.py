from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

firefox = webdriver.Firefox()
firefox.get("http://the-internet.herokuapp.com/entry_ad")
sleep(3)
close = firefox.find_element(
        By.CSS_SELECTOR, ("div[class='modal-footer']")).click()
print("закрыто окно")
firefox.quit()
