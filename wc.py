import requests
from bs4 import BeautifulSoup

def wc():
        word = raw_input("Enter your search \n")
        url = 'https://www.youtube.com/results?search_query=' +word
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html5lib")
        for link in soup.findAll('a',{'class':' yt-uix-sessionlink spf-link '}):
            href="https://youtube.com" +link.get('href')
            title=link.string
            print(href)
            print(title)
            print("\n")
            print('===========================================')
wc()