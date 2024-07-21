from selenium import webdriver

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    chrome.get("http://uitestingplayground.com/classattr")
    firefox.get("http://uitestingplayground.com/classattr")

    # Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.
    for i in range(3):
    # Кликните на синюю кнопку
        blue_button = chrome.find_element("xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
        blue_button = firefox.find_element("xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()

    # Кликаем на ок во всплывающем окне
        chrome.switch_to.alert.accept()
        firefox.switch_to.alert.accept()

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()