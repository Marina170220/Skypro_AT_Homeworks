from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

chrome.get("http://the-internet.herokuapp.com/entry_ad")

# Ждем, пока модальное окно не появится и кнопка "Close" станет кликабельной
chrome_wait = WebDriverWait(chrome, 5)
    
modal_window = chrome_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))

chrome_close_button = chrome_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer")))
sleep(1)

# В модальном окне нажмите на кнопку Close
chrome_close_button.click()
sleep(1)

chrome.quit()
