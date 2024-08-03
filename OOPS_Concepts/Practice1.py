# Implement a Book class where books are compared based on their title and author. Include all comparison methods.

class Book:
    def __init__(self, title, name, author, publication):
        self.title = title
        self.name = name
        self.author = author
        self.publication = publication


    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.title, self.name, self.author, self.publication) == (other.title, other.name, other.author, other.publication)

        return False


    def __hash__(self):
        return hash((self.title, self.name, self.author, self.publication))

    def __le__(self, other):
        if isinstance(other, Book):
            return (self.title, self.author) <= (other.title, other.author)

        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Book):
            return (self.title, self.author) < (other.title, other.author)

        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Book):
            return (self.title, self.author) >= (other.title, other.author)

        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Book):
            return (self.title, self.author) > (other.title, other.author)

        return NotImplemented

    def __repr__(self):
        return f"Book(title='{self.title}', name='{self.name}', author='{self.author}', publication={self.publication})"


# Test cases
b1 = Book("The Great Gatsby", "Novel", "F. Scott Fitzgerald", 1925)
b2 = Book("To Kill a Mockingbird", "Novel", "Harper Lee", 1960)
b3 = Book("1984", "Novel", "George Orwell", 1949)
b4 = Book("The Great Gatsby", "Novel", "F. Scott Fitzgerald", 1925)

# Equality
print(b1 == b4)  # True
print(b1 == b2)  # False

# Hash
print(hash(b1) == hash(b4))  # True
print(hash(b1) == hash(b2))  # False

# Ordering
print(b1 < b2)   # True (because "The Great Gatsby" < "To Kill a Mockingbird")
print(b1 > b2)   # False
print(b3 <= b2)  # True (because "1984" < "To Kill a Mockingbird")
print(b2 >= b1)  # True

# Sorting
books = [b2, b3, b1]
sorted_books = sorted(books)
print(sorted_books)  # [Book(1984, Novel, George Orwell, 1949), Book(The Great Gatsby, Novel, F. Scott Fitzgerald, 1925), Book(To Kill a Mockingbird, Novel, Harper Lee, 1960)]
