from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()

firefox.get("http://the-internet.herokuapp.com/inputs")

input_field = firefox.find_element(By.TAG_NAME, "input")
input_field.send_keys("1000")
sleep(1)
input_field.clear()

input_field = firefox.find_element(By.TAG_NAME, "input")
input_field.send_keys("999")
sleep(1)

firefox.quit()
