import requests as rq
from  bs4 import BeautifulSoup as bs
import pandas as pd


# Function to scrape book details from a given URL
def scrapping_books(url):
    try:
        # Sending a GET request to the URL with a timeout of 10 seconds
        response = rq.get(url, timeout=10)

        # Checking if the request was successful (status code 200)
        response.raise_for_status()
    except rq.exceptions.RequestException as e:
        print("Erreur :", e)
        return None

    # Parsing the content of the page with BeautifulSoup
    soup = bs(response.content, "html.parser")

    # each book is wrapped in an <article> tag
    books = soup.find_all("article", class_= "product_pod")

    book_list =[]

    for book in books:
        # Extracting the book title, default value "No Title" if not found
        title = book.h3.a.get("title", "No Title")
        # Extracting the book rating, default value "No Rating" if not found
        rating = book.p.get("class", ["", "No Rating"])[1]
        # Extracting the book price, default value "No Price" if not found
        price = book.find("p", class_="price_color").text.strip() if book.find("p", class_="price_color") else "No Price"

        # Appending the book details as a dictionary to the list
        book_list.append({"Title": title, "Rating": rating, "Price": price})
    
    return book_list

def main():
     
    url = "https://books.toscrape.com/"
    books_data = scrapping_books(url)

    # If data is scraped successfully, create a DataFrame and save it to an Excel file
    if books_data:
        df_book = pd.DataFrame(books_data)
        df_book.to_excel("books.xlsx", index=False)
        print("Scraping completed successfully! Data saved in 'books.xlsx'.")
    else:
        print("No data scraped. Please check the URL or try again later!!")


if __name__ == "__main__":
     main()
