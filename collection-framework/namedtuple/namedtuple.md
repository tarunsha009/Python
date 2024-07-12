### Namedtuple in Python

#### What is `namedtuple`?

A `namedtuple` is a factory function for creating tuple subclasses with named fields. It is part of Python's `collections` module. Unlike a regular tuple where elements are accessed by index, elements in a `namedtuple` can also be accessed by name, providing better readability and self-documenting code.

#### Why use `namedtuple`?

- **Readability**: Named fields make the code more readable and understandable.
- **Immutability**: Like tuples, `namedtuple` instances are immutable, meaning their values cannot be changed once set.
- **Memory-efficient**: `Namedtuple` instances are just as memory efficient as regular tuples.

#### Where to use `namedtuple`?

- When you need a lightweight, immutable data structure.
- When you want to improve code readability by using named fields.
- When you need to replace simple classes that store data without behavior.

#### Special Conditions or Situations

- Use `namedtuple` when you need a simple, immutable object with named fields.
- Avoid `namedtuple` if you need to mutate the fields or if you require methods beyond simple data storage.

#### Syntax

```python
from collections import namedtuple

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create instances of the namedtuple
p1 = Point(11, 22)
p2 = Point(33, 44)

# Access elements by name
print(p1.x, p1.y)  # Output: 11 22
print(p2.x, p2.y)  # Output: 33 44

# Access elements by index
print(p1[0], p1[1])  # Output: 11 22
print(p2[0], p2[1])  # Output: 33 44
```

#### Example

1. **Creating a `namedtuple` for a Point:**
   ```python
   from collections import namedtuple

   Point = namedtuple('Point', ['x', 'y'])
   p = Point(11, 22)
   print(p.x, p.y)  # Output: 11 22
   ```

2. **Using a `namedtuple` for a Book:**
   ```python
   from collections import namedtuple

   Book = namedtuple('Book', ['title', 'author', 'year'])
   book1 = Book('1984', 'George Orwell', 1949)
   book2 = Book('To Kill a Mockingbird', 'Harper Lee', 1960)

   print(book1.title, book1.author, book1.year)  # Output: 1984 George Orwell 1949
   print(book2.title, book2.author, book2.year)  # Output: To Kill a Mockingbird Harper Lee 1960
   ```

#### Advantages of `namedtuple`

- **Named Access**: Provides attribute access to elements, making the code more readable.
- **Documentation**: Serves as a self-documenting code because the field names indicate what the data represents.
- **Immutability**: The immutability characteristic ensures data integrity.
- **Efficiency**: As memory-efficient as regular tuples.

#### Practical Exercises

1. **Exercise 1: Create a `namedtuple` for storing information about a student (name, age, grade).**
   ```python
   from collections import namedtuple

   Student = namedtuple('Student', ['name', 'age', 'grade'])
   student1 = Student('Alice', 20, 'A')
   student2 = Student('Bob', 22, 'B')

   print(student1.name, student1.age, student1.grade)  # Output: Alice 20 A
   print(student2.name, student2.age, student2.grade)  # Output: Bob 22 B
   ```

2. **Exercise 2: Create a `namedtuple` to store information about a movie (title, director, year).**
   ```python
   from collections import namedtuple

   Movie = namedtuple('Movie', ['title', 'director', 'year'])
   movie1 = Movie('Inception', 'Christopher Nolan', 2010)
   movie2 = Movie('The Matrix', 'The Wachowskis', 1999)

   print(movie1.title, movie1.director, movie1.year)  # Output: Inception Christopher Nolan 2010
   print(movie2.title, movie2.director, movie2.year)  # Output: The Matrix The Wachowskis 1999
   ```

3. **Exercise 3: Create a list of `namedtuple` instances for books and print the titles of books published after a given year.**
   ```python
   from collections import namedtuple

   Book = namedtuple('Book', ['title', 'author', 'year'])
   books = [
       Book('1984', 'George Orwell', 1949),
       Book('To Kill a Mockingbird', 'Harper Lee', 1960),
       Book('Brave New World', 'Aldous Huxley', 1932)
   ]

   year_threshold = 1940
   for book in books:
       if book.year > year_threshold:
           print(book.title)
   # Output:
   # To Kill a Mockingbird
   # 1984
   ```
