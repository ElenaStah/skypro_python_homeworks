from selenium import webdriver
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.implicitly_wait(10)
logging.basicConfig(level=logging.INFO)
# Вывод информации о начале теста
logging.info("Начало теста: Ожидание видимости элемента.")
driver.get('http://uitestingplayground.com/textinput')
driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(button)
