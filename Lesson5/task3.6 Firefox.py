from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()

firefox.get("http://the-internet.herokuapp.com/login")
    
input_name = firefox.find_element(By.ID, "username").send_keys("tomsmith")
sleep(1)

input_pass = firefox.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
sleep(1)

button = firefox.find_element(By.TAG_NAME, "button").click()
sleep(1)

firefox.quit()
