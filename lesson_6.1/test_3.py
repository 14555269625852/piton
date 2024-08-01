from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form():
    chrome = webdriver.Firefox()
    chrome.get("https://www.saucedemo.com/")

    chrome.find_element(By.NAME, ("user-name")).send_keys("standard_user")
    chrome.find_element(By.NAME, ("password")).send_keys("secret_sauce")
    chrome.find_element(By.NAME, ("login-button")).click()
    chrome.find_element(By.NAME, ("add-to-cart-sauce-labs-backpack")).click()
    chrome.find_element(
        By.NAME, ("add-to-cart-sauce-labs-bolt-t-shirt")).click()
    chrome.find_element(By.NAME, ("add-to-cart-sauce-labs-onesie")).click()
    chrome.find_element(
        By.CSS_SELECTOR, ('a[class="shopping_cart_link"]')).click()
    chrome.find_element(By.NAME, ("checkout")).click()
    chrome.find_element(By.ID, ("first-name")).send_keys("Светлана")
    chrome.find_element(By.ID, ("last-name")).send_keys("Юшкова")
    chrome.find_element(By.ID, ("postal-code")).send_keys("123456")
    chrome.find_element(By.ID, ("continue")).click()
    total_price = chrome.find_element(By.CLASS_NAME, ('summary_total_label'))
    total = total_price.text.strip().replace("Total: $", "")
    ex_total = "58.29"
    assert total == ex_total
    chrome.quit()
