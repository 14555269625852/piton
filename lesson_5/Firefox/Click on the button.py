from selenium import webdriver
from selenium.webdriver.common.by import By


firefox = webdriver.Firefox()
firefox.get("https://the-internet.herokuapp.com/add_remove_elements/")

for x in range(1, 6):
    click_on_button = firefox.find_element(
        By.CSS_SELECTOR, ("[onclick='addElement()']")).click()
    firefox_delete_buttons = firefox.find_elements(
        By.XPATH, "//button[@onclick='deleteElement()']")
print(f"Размер спика кнопок Delete in Firefox:{len(firefox_delete_buttons)}")

firefox.quit()
