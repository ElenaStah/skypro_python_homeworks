 	from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

#открыть сайт
driver.get("http://uitestingplayground.com/classattr") 
Add_Element = "button.btn-primary"
click = driver.find_element(By.CSS_SELECTOR, Add_Element)

#Трижды кликнуть по синей кнопке
for n in range(3):
       click.click()
       a = driver.switch_to.alert.accept()
       sleep(1)
sleep(5)	
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

#открыть сайт
driver.get("http://uitestingplayground.com/classattr")
Add_Element = "button.btn-primary"
click = driver.find_element(By.CSS_SELECTOR, Add_Element)

#Трижды кликнуть по синей кнопке
for n in range(3):
       click.click()
       a = driver.switch_to.alert.accept()
       sleep(1)
sleep(5)	
driver.quit() 	
