
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://boniqarcia.dev/selenium-webdriver-java/loading-images.html')
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#landscape")))
scr = driver.find_element(By.CSS_SELECTOR, "#award")

print(scr.get_attribute('scr'))