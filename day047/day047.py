#Day 47

class Library:
    def __init__(self, book, shelf):
        self.book = book
        self.shelf = shelf

class Science_Section(Library):
    def __init__(self,  book, shelf):
        super().__init__(book, shelf)
        
        self.name = 'Physics books'

science = Science_Section(20, 4)
print(science.book, science.shelf, science.name)

