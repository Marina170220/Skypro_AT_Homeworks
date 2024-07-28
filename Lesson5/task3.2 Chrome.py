from selenium import webdriver

chrome = webdriver.Chrome()

count=0
chrome.get("http://uitestingplayground.com/dynamicid")

# Кликните на синюю кнопку
blue_button = chrome.find_element("xpath", '//button[text()="Button with Dynamic ID"]').click()

# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково
for i in range(3):
    blue_button = chrome.find_element("xpath", '//button[text()="Button with Dynamic ID"]').click()
    count += 1
    print(count)

chrome.quit()
