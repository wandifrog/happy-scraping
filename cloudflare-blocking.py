print(123)

from bs4 import BeautifulSoup
import requests
import lxml
import cloudscraper

url = 'https://bacakomik.co/one-piece-chapter-001-bahasa-indonesia/'

agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
page = requests.get(url, headers=agent)
print (BeautifulSoup(page.content, 'lxml'))

# scraper = cloudscraper.create_scraper()
# html = scraper.get(url).content
# soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# source = requests.get(url).text
# soup = BeautifulSoup(source, 'lxml')

# imageWrapper = soup.find("div", class_='chapter-area')

# print(soup)
# print(imageWrapper)
