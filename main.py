
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service(r'C:\Users\PrashantG\PycharmProjects\Scrappy\Drivers\chromedriver.exe')
driver=webdriver.Chrome(service=s)
driver.get("https://www.amazon.in/")
driver.maximize_window()
element=driver.find_element("id","twotabsearchtextbox")
element.send_keys("Headphone")
driver.find_element("id","nav-search-submit-button").click()
driver.find_element('xpath','//*[@id="p_89/boAt"]/span/a/div/label/i').click()
driver.find_element('xpath','//*[@id="a-autoid-0-announce"]').click()
driver.find_element('xpath','//*[@id="s-result-sort-select_3"]').click()

for i in range(3,10):
    a=driver.find_element('xpath','//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div["+i+"]/div/div/div/div/div[2]/div[1]/h2/a/span')
    name=a.text
    print(name)
''' b=driver.find_element('xpath','//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[i]/div/div/div/div/div[2]/div[3]/div[2]/a/span[1]/span[2]/span[2]')
    price=b.text

    print(name+","+price)
'''


