from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
LOGIN_BUTTON = (By.XPATH, '//*[@aria-label="Войти"]')
EMAIL_FIELD = (By.XPATH, '//*[@type="email"]')
NEXT_BUTTON = (By.XPATH, '//*[@id="identifierNext"]')
ERROR_TEXT = (By.XPATH, '//*[text()="Введите адрес электронной почты или номер телефона."]')
MAIL_BUTTON = (By.XPATH, '//*[@aria-label="Почта (откроется новая вкладка)"]')
SIGH_IN = (By.XPATH, '//*[@data-action="sign in"]')
PICTURE_BUTTON = (By.XPATH, '//*[@aria-label="Поиск картинок (откроется новая вкладка)"]')
GOOGLE_PICTURE = (By.XPATH,'//*[@class="T8VaVe"]')

def find_element(driver, locator, time=5):
    return WebDriverWait(driver, time).until(expected_conditions.presence_of_element_located(locator))

def test_error_auth():
    driver.get("https://google.com")
    find_element(driver, LOGIN_BUTTON).click()
    # find_element(driver, EMAIL_FIELD).send_keys("mail")
    find_element(driver,NEXT_BUTTON).click()
    find_element(driver, ERROR_TEXT)

def test_error_email():
    driver.get("https://google.com")
    find_element(driver, MAIL_BUTTON).click()
    find_element(driver, SIGH_IN).click()
    find_element(driver, NEXT_BUTTON).click()
    find_element(driver,ERROR_TEXT)

def test_text_picture():
    driver.get("https://google.com")
    find_element(driver, PICTURE_BUTTON).click()
    find_element(driver,GOOGLE_PICTURE)







