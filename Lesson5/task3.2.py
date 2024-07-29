from selenium import webdriver

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    count=0
    chrome.get("http://uitestingplayground.com/dynamicid")
    firefox.get("http://uitestingplayground.com/dynamicid")

    # Кликните на синюю кнопку
    blue_button = chrome.find_element("xpath", '//button[text()="Button with Dynamic ID"]').click()
    blue_button = firefox.find_element("xpath", '//button[text()="Button with Dynamic ID"]').click()

    # Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково
    for i in range(3):
        blue_button = chrome.find_element("xpath", '//button[text()="Button with Dynamic ID"]').click()
        blue_button = firefox.find_element("xpath", '//button[text()="Button with Dynamic ID"]').click()
        count += 1
        print(count)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()