import requests
from bs4 import BeautifulSoup
import csv

def parsing():
    url = "https://books.toscrape.com"
    response = requests.get(url=url)

    soup = BeautifulSoup(response.text,"html.parser")
    books = soup.find_all("article", class_ = "product_pod")

    book_list =[]

    for book in books:
        title = book.h3.a['title']


        stock = book.find('p', class_ = 'instock availability').text.strip()

        price =  book.find('p',class_='price_color').text   
        
        book_info = f"📖 **{title}**\n💰 Цена: {price}\n✅ Статус: {stock}"
        book_list.append(book_info)
    return "\n\n" + "\n───────────────\n".join(book_list)
        

    
