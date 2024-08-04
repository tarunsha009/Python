class Book:

    def __init__(self, name, author):
        self.name = name
        self.author = author

    @classmethod
    def from_title(cls, name, title):
        author = title.split('-')[1]
        return cls(name, author)


b = Book("Design Patterns", "Tarun Sharma")

cb = Book.from_title("New Life", "NewLife-Anshul Sharma")

print(b.name, b.author)

print(cb.name, cb.author)