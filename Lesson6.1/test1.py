from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from data import *
from time import sleep


def test_types_form(chrome_browser):
    chrome_browser.get(URL_1)
    form_data = {
        "first-name": first_name,
        "last-name": last_name,
        "address": address,
        "e-mail": email,
        "phone": phone,
        "zip-code": zip_code,
        "city": city,
        "country": country,
        "job-position": job_position,
        "company": company
    }

    for key, value in form_data.items():
        chrome_browser.find_element(By.NAME, key).send_keys(value)

    WebDriverWait(chrome_browser, 30, 0.1).until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
    sleep(3)

    field_classes = {
        "zip-code": "danger",
        "first-name": "success",
        "last-name": "success",
        "address": "success",
        "e-mail": "success",
        "phone": "success",
        "city": "success",
        "country": "success",
        "job-position": "success",
        "company": "success"
    }

    for field_id, class_name in field_classes.items():
        assert class_name in chrome_browser.find_element(By.ID, field_id).get_attribute("class")
