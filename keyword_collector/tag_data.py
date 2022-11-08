class TagData(dict):
    def __init__(self, source, date, tag):
        self.source = source
        self.date = date
        self.tag = tag

    def to_dict(self):
        return self.__dict__
