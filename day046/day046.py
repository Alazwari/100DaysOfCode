#Day 46

class Library:
    def __init__(self):
        self.book = 300
        self.shelf = 45

class Science_Section(Library):
    def __init__(self):
        super().__init__()
        self.name = 'Physics books'

science = Science_Section()
print(science.book, science.shelf, science.name)