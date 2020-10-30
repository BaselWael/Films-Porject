class query_term:
    def __init__(self,film_name = None):
        self.film_name = film_name

    def Check(self):
        name = ""
        for i in self.film_name:
            if i != " ":
                name+=i
            else:
                name+="%20"
        return name