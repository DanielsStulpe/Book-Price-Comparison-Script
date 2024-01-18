import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.janisroze.lv/lv/"
driver.get(url)
time.sleep(2)

book = "Zēns, kuram patika brieži"

search_input = driver.find_element(By.ID, "search")
search_input.send_keys(book)
input_butt = driver.find_element(By.CLASS_NAME, "button")
input_butt.click()
s_book = driver.find_element(By.CLASS_NAME, "product-name")
s_book.click()

book_price = driver.find_element(By.CLASS_NAME, "price").text
print(book_price)

input()