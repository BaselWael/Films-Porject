import requests
from bs4 import BeautifulSoup
url = 'https://subscene.com/subtitles/iron-man-3'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
a = soup.find_all('span')
print(a)