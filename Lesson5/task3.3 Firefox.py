from selenium import webdriver

firefox = webdriver.Firefox()

firefox.get("http://uitestingplayground.com/classattr")

# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.
for i in range(3):
 # Кликните на синюю кнопку
    blue_button = firefox.find_element("xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()

# Кликаем на ок во всплывающем окне
    firefox.switch_to.alert.accept()

firefox.quit()
