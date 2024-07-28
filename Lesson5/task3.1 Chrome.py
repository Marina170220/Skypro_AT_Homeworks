from selenium import webdriver

chrome = webdriver.Chrome()

chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Пять раз кликните на кнопку Add Element
for i in range(5):
    add_button = chrome.find_element("xpath", '//button[text()="Add Element"]').click()

# Соберите со страницы список кнопок Delete
    chrome_delete_buttons = chrome.find_elements("xpath", '//button[text()="Delete"]')

# Выведите на экран размер списка
print(f"Размер списка кнопок Delete в Chrome: {len(chrome_delete_buttons)}")

chrome.quit()
