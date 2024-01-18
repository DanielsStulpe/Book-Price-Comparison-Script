import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

books_list = ["Zēns, kuram patika brieži", "Dzeguzēns", "Uz paradīzi"]

def janisroze_price(books):
    url = "https://www.janisroze.lv/lv/"
    driver.get(url)
    time.sleep(2)

    for book in books:
        search_input = driver.find_element(By.ID, "search")
        search_input.clear()
        search_input.send_keys(book)
        input_butt = driver.find_element(By.CLASS_NAME, "button")
        input_butt.click()
        time.sleep(2)

        book_price = driver.find_element(By.CLASS_NAME, "price").text
        price =  float(book_price[1::].replace(",", "."))
        print(price)


janisroze_price(books_list)