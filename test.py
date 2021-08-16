import random
import time 
from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\aivan\\Desktop\\Python_programs\\Selenium\\chromedriver.exe')
url = "https://www.olx.com.ec/autos_c378"
driver.get(url)

#Todos los anuncions en una lista
autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

for auto in autos:
    print(auto)
