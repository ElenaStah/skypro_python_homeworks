from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
#открыть сайт
driver.get("http://uitestingplayground.com/dynamicid")

#кликнуть на кнопку "Add element" 3 раза

Add_button = "button.btn-primary"
click = driver.find_element(By.CSS_SELECTOR, Add_button)
for n in range(3):
       click.click()
       a = driver.switch_to.alept.accept()
       sleep(1)
sleep(5)
	
driver.quit()

## открыть страницу в FireFox
# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager().install())
# driver = webdriver.Firefox(executable_path = GeckoDriverManager().install())

#открыть сайт
driver.get("http://uitestingplayground.com/dynamicid")

#кликнуть на кнопку "Add element" 3 раза

Add_button = "button.btn-primary"
click = driver.find_element(By.CSS_SELECTOR, Add_button)
for n in range(3):
       click.click()
       a = driver.switch_to.alept.accept()
       sleep(1)
sleep(5)
	
driver.quit() 	