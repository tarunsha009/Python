class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state

    def __eq__(self, other):
        if isinstance(other, Address):
            return self.city == other.city and self.state == other.state
        return False

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age and self.address == other.address
        return False

address1 = Address("New York", "NY")
address2 = Address("New York", "NY")
p1 = Person("Alice", 30, address1)
p2 = Person("Alice", 30, address2)

print(p1 == p2)  # True
