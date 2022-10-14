from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

s = Service(r'C:\Users\PrashantG\PycharmProjects\Scrappy\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=s)
#driver.implicitly_wait(10)
driver.get('https://www.google.com')
driver.maximize_window()
element= driver.find_element("name","q")
element.send_keys("Hello")
print(element.get_attribute("title"))
print(element.is_displayed())
#element.submit()
driver.quit()





