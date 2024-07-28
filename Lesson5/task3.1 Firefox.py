from selenium import webdriver

firefox = webdriver.Firefox()


firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Пять раз кликните на кнопку Add Element
for i in range(5):
    add_button = firefox.find_element("xpath", '//button[text()="Add Element"]').click()

# Соберите со страницы список кнопок Delete
    firefox_delete_buttons = firefox.find_elements("xpath", '//button[text()="Delete"]')

# Выведите на экран размер списка
print(f"Размер списка кнопок Delete в Firefox: {len(firefox_delete_buttons)}")

firefox.quit()