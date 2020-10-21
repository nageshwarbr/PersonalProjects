from bs4 import BeautifulSoup
import requests

# with open('simple.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
# print(soup.prettify())
# match = soup.title.text
# print(match)
# match = soup.find('div', class_='footer')
# print(match)
# article = soup.find_all('div', class_='article')
# for headlines in article:
#     print(headlines.h2.a.text)
source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml').text

