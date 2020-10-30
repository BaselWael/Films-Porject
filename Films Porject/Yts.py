from urllib.request import Request, urlopen
import urllib.request
import json
from Quert_Term import query_term
from limit import Limit


class Movie():
    def __init__(self,filmname,url = None,limit = None):
        self.filmname = filmname
        self.url = url
        self.url = "https://yts.mx/api/v2/list_movies.json?"
        self.Limit = limit

    def getdata(self):
        Query_Term = query_term(film_name=self.filmname).Check()
        limit = Limit(limit=self.Limit).Check()
        urll = self.url + "&query_term=" + str(Query_Term)+'&limit=' + str(limit)
        try:
            openurl = Request(urll, headers={'User-Agent': 'Mozilla/5.0'})
            web_page_open = urlopen(openurl).read()
            global j
            j = json.loads(web_page_open)
        except Exception:
            print("No Internet Connection!")
        try:
            data = j['data']['movies']
            trailer_url = 'https://www.youtube.com/watch?v='
            for i in data:
                print(i["title"])
                torrent_data = i['torrents']
                print("Trailer : ", trailer_url + i['yt_trailer_code'])
                for x in torrent_data:
                    print(x["quality"])
                    print(x['size'])
                    print(x['type'])
                    print('url : ', x['url'])
        except Exception:
            print("No Data Found")

