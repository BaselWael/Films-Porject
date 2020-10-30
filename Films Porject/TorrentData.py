from urllib.request import Request, urlopen
import json
from Quert_Term import query_term
from limit import Limit
class torrent:
    def __init__(self,film_name=None,limit=None):
        self.film_name = film_name
        self.limit = limit

    def Urlbase(self):
        return "https://yts.mx/api/v2/list_movies.json?"


    def item(self): # return film name
        Film_name_text = open('Filmname.txt', "r")
        item = Film_name_text.read()
        return item
    
    def GetTorrentUrl(self,quality,type,size):# return url
        Query_Term = query_term(film_name=self.item()).Check()
        limit = str(Limit(limit=50).Check())
        url = self.Urlbase()
        urll = (url + 'query_term={}&limit={}'.format(Query_Term, limit))
        try:
            openurl = Request(urll, headers={'User-Agent': 'Mozilla/5.0'})
            web_page_open = urlopen(openurl).read()
            global j
            j = json.loads(web_page_open)
        except Exception:
            return "No Connection!"
        try:
            data = j['data']['movies']
            item = self.item()
            for i in data:
                if i['title'] == item:
                    for x in i['torrents']:
                        url = x['url']
                        if x['type'] ==type and x['size'] ==size and x['quality'] == quality :
                            return url
        except Exception:
            return 'No Url found'

    def GetTorrentSize(self, quality, type, size): #return size
            Query_Term = query_term(film_name=self.item()).Check()
            limit = str(Limit(limit=50).Check())
            url = self.Urlbase()
            urll = (url + 'query_term={}&limit={}'.format(Query_Term, limit))
            try:
                openurl = Request(urll, headers={'User-Agent': 'Mozilla/5.0'})
                web_page_open = urlopen(openurl).read()
                global j
                j = json.loads(web_page_open)
            except Exception:
                return "No Connection!"
            try:
                data = j['data']['movies']
                item = self.item()
                for i in data:
                    if i['title'] == item:
                        for x in i['torrents']:
                            sizee = x['size']
                            if x['type'] == type and x['size'] == size and x['quality'] == quality:
                                return sizee
            except Exception:
                return "No size found"

    def GetQuality(self): # return list of quality
        Query_Term = query_term(film_name=self.item()).Check()
        limit = str(Limit(limit=50).Check())
        url = self.Urlbase()
        urll = (url + 'query_term={}&limit={}'.format(Query_Term, limit))
        try:
            openurl = Request(urll, headers={'User-Agent': 'Mozilla/5.0'})
            web_page_open = urlopen(openurl).read()
            global j
            j = json.loads(web_page_open)
        except Exception:
            return ["No Connection!"]
        try:
            data = j['data']['movies']
            item = self.item()
            for i in data:
                if i['title'] == item:
                    lst = []
                    for x in i['torrents']:
                        lst.append(x['quality'])
                    return lst
        except Exception:
            return ["No quality found"]

    def GetType(self): # return type of movie(bluray , hdcam)
        Query_Term = query_term(film_name=self.item()).Check()
        limit = str(Limit(limit=50).Check())
        url = self.Urlbase()
        urll = (url + 'query_term={}&limit={}'.format(Query_Term, limit))
        try:
            openurl = Request(urll, headers={'User-Agent': 'Mozilla/5.0'})
            web_page_open = urlopen(openurl).read()
            global j
            j = json.loads(web_page_open)
        except Exception:
            return ["No Connection!"]
        try:
            data = j['data']['movies']
            item = self.item()
            for i in data:
                if i['title'] == item:
                    lst = []
                    for x in i['torrents']:
                        lst.append(x['type'])
                    return lst
        except Exception:
            return ["No type found"]
    def GetSize(self):
        Query_Term = query_term(film_name=self.item()).Check()
        limit = str(Limit(limit=50).Check())
        url = self.Urlbase()
        urll = (url + 'query_term={}&limit={}'.format(Query_Term, limit))
        try:
            openurl = Request(urll, headers={'User-Agent': 'Mozilla/5.0'})
            web_page_open = urlopen(openurl).read()
            global j
            j = json.loads(web_page_open)
        except Exception:
            return ["No Connection!"]
        try:
            data = j['data']['movies']
            item = self.item()
            for i in data:
                if i['title'] == item:
                    lst = []
                    for x in i['torrents']:
                        lst.append(x['size'])
                    return lst
        except Exception:
            return "No quality found"

    def GetFilmNames(self): # return film name
        Query_Term = query_term(film_name=self.film_name).Check()
        limit = str(Limit(limit=self.limit).Check())
        url = self.Urlbase()
        urll = (url+'query_term={}&limit={}'.format(Query_Term,limit))
        try:
            openurl = Request(urll, headers={'User-Agent': 'Mozilla/5.0'})
            web_page_open = urlopen(openurl).read()
            global j
            j = json.loads(web_page_open)
        except Exception:
            return ["No Connection!"]
        try:
            data = j['data']['movies']
            lst = []
            for i in data:
                lst.append(i['title'])
            return lst
        except Exception:
            return ["No Url Found"]
