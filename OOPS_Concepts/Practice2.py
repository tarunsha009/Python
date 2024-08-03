# Define a Person class where persons are compared based on their age. Implement comparison methods for equality,
# less than, and greater than.
class Address:

    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode


    def __eq__(self, other):
        if isinstance(other, Address):
            return (self.street, self.city, self.state, self.zipcode) == (other.street, other.city, other.state, other.zipcode)
        return False

    def __hash__(self):
        return hash((self.street, self.city, self.state, self.zipcode))

class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __eq__(self, other):
        if isinstance(other, Person):
            return (self.age) == (other.age)
        return False

    def __hash__(self):
        return hash((self.age))

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Person):
            return self.age <= other.age
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Person):
            return self.age > other.age
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Person):
            return self.age >= other.age
        return NotImplemented


# Test cases
address1 = Address("123 Main St", "Springfield", "IL", "62701")
address2 = Address("456 Elm St", "Springfield", "IL", "62701")

person1 = Person("Alice", 30, address1)
person2 = Person("Bob", 25, address2)
person3 = Person("Charlie", 30, address1)
person4 = Person("Alice", 30, address1)

print(person1 == person4)  # True, same name, age, and address
print(person1 == person3)  # False, different names
print(person1 < person2)   # False, because 30 > 25
print(person1 > person2)   # True, because 30 > 25
print(person1 >= person4)  # True, because they are equal
print(person2 <= person3)  # True, because 25 < 30
print(person1 == person2)  # False, different ages and names

# Additional test cases for Address comparison
print(address1 == address2)  # False, different street
print(address1 == Address("123 Main St", "Springfield", "IL", "62701"))  # True, same address