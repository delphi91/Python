#Program takes headers of news from the website
#need to instal bs4 and requests packages
import requests
from bs4 import BeautifulSoup

def headersList():
    url = 'http://www.interia.pl' #need some url address
    r = requests.get(url)
    source = BeautifulSoup(r.text, features ="html.parser")

    for header in source.find_all(class_="news-li"): #name of class in html code of our website
        if header.a: #if header is a link
            print(header.a.text.replace("\n", " ").strip())
        else:
            print(header.contents[0].strip())

#Headers number
def headersTable():
    url = 'http://www.interia.pl/'
    titles = []

    url = requests.get(url)
    soup = BeautifulSoup(url.text, features="html.parser")
    title = soup.findAll('li', {'class': 'news-li'})
    for row in title:
        titles.append(row.text.replace("\n", " ").strip())
    print('There are',len(titles),'headers.')

print('List of headers')
headersList()
headersTable()
