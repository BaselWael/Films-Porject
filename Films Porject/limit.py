class Limit:
    def __init__(self,limit):
        self.limit = limit

    def Check(self):
        if self.limit < 1:
            self.limit = 1
            return self.limit
        elif self.limit > 50:
            self.limit = 50
            return self.limit
        else:
            return self.limit