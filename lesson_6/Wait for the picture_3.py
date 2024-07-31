from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome = webdriver.Firefox()
wait = WebDriverWait(chrome, 40, 0.1)

chrome.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
wait.until(EC.text_to_be_present_in_element((By.ID, "text"), 'Done!'))

print(chrome.find_element(By.ID, "award").get_attribute("src"))

chrome.quit()
