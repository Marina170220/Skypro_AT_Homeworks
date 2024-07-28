from selenium import webdriver

firefox = webdriver.Firefox()

count=0
firefox.get("http://uitestingplayground.com/dynamicid")

# Кликните на синюю кнопку
blue_button = firefox.find_element("xpath", '//button[text()="Button with Dynamic ID"]').click()

# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково
for i in range(3):
    blue_button = firefox.find_element("xpath", '//button[text()="Button with Dynamic ID"]').click()
    count += 1
    print(count)

firefox.quit()
