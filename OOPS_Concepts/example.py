class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

    def __hash__(self):
        return hash((self.name, self.age))

p1 = Person("Alice", 30)
p2 = Person("Alice", 30)

people = {p1, p2}

print(p1 == p2)