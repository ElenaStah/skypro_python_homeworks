from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 40, 0.1)

driver.get('http://uitestingplayground.com/ajax')
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# Дождаться появления текста в зеленой плашке и затем продолжить
try:green_box_text = WebDriverWait(driver, 16).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))).text
except TimeoutException:
    print("Элемент не был найден в отведенное время.")
print(green_box_text) 
