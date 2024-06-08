from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

#открыть ccылку
driver.get("http://the-internet.herokuapp.com/login")
driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys("tomsmith")
driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, 'i.fa').click()

sleep(2)	
driver.quit()

## открыть страницу в FireFox
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(service=FirefoxService(
GeckoDriverManager().install()))

#открыть ccылку
driver.get("http://the-internet.herokuapp.com/login")
driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys("tomsmith")
driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, 'i.fa').click()

sleep(2)	
driver.quit()
