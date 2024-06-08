from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

#открыть сайт
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

#кликнуть на кнопку "Add element" 5 раз
add_button = "button"
five_button = driver.find_element(By.CSS_SELECTOR, add_button)

for n in range(5):
       five_button.click()
sleep(1)
sleep(5)

#вывести в консоль размер списка
delete_button = driver.find_elements(By.CSS_SELECTOR, ".added-manually" )
print(len(delete_button))
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
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

#кликнуть на кнопку "Add element" 5 раз
add_button = "button"
five_button = driver.find_element(By.CSS_SELECTOR, add_button)

for n in range(5):
       five_button.click()
sleep(1)
sleep(5)

#вывести в консоль размер списка
delete_button = driver.find_elements(By.CSS_SELECTOR, ".added-manually" )
print(len(delete_button))
sleep(5)
	
driver.quit()
