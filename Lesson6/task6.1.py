from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20, 0.1)

try:
    driver.get("http://uitestingplayground.com/ajax")
    blue_button = driver.find_element(By.CSS_SELECTOR,"#ajaxButton").click()
    print(wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))).text)

except Exception as ex:
    print(ex)
finally:
    driver.quit()
