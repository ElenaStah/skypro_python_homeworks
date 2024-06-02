from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

#открыть сайт
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)

#кликнуть на кнопку 
button = driver.find_element(By.CSS_SELECTOR, "div.modal - footer p").click()
       
sleep(5)	
driver.quit()

## открыть страницу в FireFox
# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager().install())
# driver = webdriver.Firefox(executable_path = GeckoDriverManager().install())
#открыть сайт
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)

#кликнуть на кнопку 
button = driver.find_element(By.CSS_SELECTOR, "div.modal - footer p").click()
       
sleep(5)	
driver.quit()
