# Importē bibliotēkas un moduļus no Selenium
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Izveido sarakstu, lai glabātu grāmatu nosaukumus
books_list = []

# Atver failu ar grāmatu nosaukumiem un ielasa tos sarakstā
with open("Automatizācija - Projekts/dip225-Projekts/books.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        books_list.append(line.rstrip())
file.close()

# Izveido Selenium servisu un izvēlnes opcijas, izmantojot Chrome pārlūku
service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

# Funkcija, lai iegūtu grāmatu cenas no janisroze.lv
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
            price = float(book_price[1::].replace(",", "."))
            books_price.append(price)
        except:
            books_price.append(1000)
        
    return books_price

# Funkcija, lai iegūtu grāmatu cenas no eglobuss.lv
def eglobuss_price(books):
    url = "https://eglobuss.lv/"
    driver.get(url)
    time.sleep(2)
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
        driver.implicitly_wait(1)

        try:
            book_price = driver.find_element(By.CLASS_NAME, "single__price").text
            price = float(book_price[1::])
            books_price.append(price)
        except:
            books_price.append(1000)
        
    return books_price

# Funkcija, lai iegūtu grāmatu cenas no valtersunrapa.lv
def valtersunrapa_price(books):
    books_price = []

    for book in books:
        try:
            url = f"https://www.valtersunrapa.lv/lv/search/?s={book}"
            driver.get(url)
            time.sleep(2)

            book_price = driver.find_element(By.CLASS_NAME, "price").text
            price = float(book_price[0:5].replace(",", "."))
            books_price.append(price)
        except:
            books_price.append(1000)

    return books_price

# Iegūst grāmatu cenas no katras grāmatnīcas un ievieto tās atbilstoša sarakstā
price_1 = janisroze_price(books_list)
price_2 = eglobuss_price(books_list)
price_3 = valtersunrapa_price(books_list)

# Ieraksta rezultātus failā
with open("Automatizācija - Projekts/dip225-Projekts/result.txt", "w", encoding="utf-8") as file:
    for i in range(0, len(books_list)):
        file.write(str(i + 1) + ". ")
        # Atradu labāko cenu un ierakstu to un vietnes nosaukumu teksta dokumentā
        if (price_1[i] == price_2[i] == price_3[i] == 1000):
            file.write(books_list[i] + " - Nav pieejams visos veikalos\n")
        elif (price_1[i] <= price_2[i] and price_1[i] <= price_3[i]):
            file.write(books_list[i] + " - " + str(price_1[i]) + "€ - janisroze.lv\n")
        elif (price_2[i] <= price_1[i] and price_2[i] <= price_3[i]):
            file.write(books_list[i] + " - " + str(price_2[i]) + "€ - eglobuss.lv\n")
        else:
            file.write(books_list[i] + " - " + str(price_3[i]) + "€ - valtersunrapa.lv\n")
file.close()

# Aizver pārlūku
driver.quit()
