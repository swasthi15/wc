import requests
from bs4 import BeautifulSoup

def wc():
        word = input("enter\n")
        url= 'https://www.youtube.com/results?search_query=' +word
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text)
        print(soup)
wc()