from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
class Sub:
    url = 'https://subscene.com/subtitles/'
    href = ''
    def Name(self,moviename):
        movie = moviename.replace(' ','-')
        data = Sub.url+movie
        Sub.href+=data
        return data

    def Data(self):
        page = requests.get(Sub.href)
        soup = BeautifulSoup(Sub.href.content)

