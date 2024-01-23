from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--enable-javascript")

url = "https://www.beerwulf.com/en-gb/c/all-beers?segment=Beers&catalogCode=Beer_1"

driver = webdriver.Chrome(options)
#access the url through a browser
driver.get(url)
#Scroll to the bottom page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#page will load new item while you scrolling    
time.sleep(5)

result = []
elements = driver.find_element(By.XPATH,'//*[@id="product-items-container"]')
elemen = elements.find_elements(By.TAG_NAME,"a")
for e in elemen:
    link = e.get_attribute('href')
    if link != None:
        result.append(link)

driver.quit()

print(result)
print(len(result))
print(type)