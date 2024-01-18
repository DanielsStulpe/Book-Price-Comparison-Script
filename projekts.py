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
    
    books_price = []

    for book in books:
        search_input = driver.find_element(By.ID, "search")
        search_input.clear()
        search_input.send_keys(book)
        input_butt = driver.find_element(By.CLASS_NAME, "button")
        input_butt.click()
        time.sleep(1.5)

        try:
            book_price = driver.find_element(By.CLASS_NAME, "price").text
            price =  float(book_price[1::].replace(",", "."))
            books_price.append(price)
        except:
            books_price.append(100)
        
    return books_price

def eglobuss_price(books):
    url = "https://eglobuss.lv/"
    driver.get(url)
    driver.implicitly_wait(1)
    cookie_butt = driver.find_element(By.CLASS_NAME, "cookieinfo-close")
    cookie_butt.click()
    
    books_price = []

    for book in books:
        search_input = driver.find_element(By.ID, "autocomplete-search")
        search_input.clear()
        search_input.send_keys(book)
        input_butt = driver.find_element(By.CLASS_NAME, "header__actions-item")
        input_butt.click()

        try:
            book_price = driver.find_element(By.CLASS_NAME, "single__price").text
            price =  float(book_price[1::])
            books_price.append(price)
        except:
            books_price.append(100)
        
    return books_price


print(janisroze_price(books_list))
print(eglobuss_price(books_list))