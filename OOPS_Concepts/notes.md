## Python OOPS Interview Questions

In this section, we will prepare for object-oriented programming (OOP) and related interview questions in Python, focusing on several key areas:

1. Object Equality and Identity
2. Custom Comparison Methods
3. Class Methods and Static Methods
4. Inheritance and Polymorphism
5. Encapsulation and Data Hiding
6. Special Methods and Operator Overloading

### Object Equality and Identity

In Python, we frequently use two concepts to compare objects: equality (`==`) and identity (`is`).

- **Equality (`==`)**: Checks if the values of two objects are the same.

    ```python
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a == b)  # True
    ```

- **Identity (`is`)**: Checks if two references point to the same object in memory.

    ```python
    a = [1, 2, 3]
    b = a
    print(a is b)  # True
    ```

Now, sometimes in your coding interview, the interviewer may ask how to compare if two objects of a custom class are equal in terms of their values. For example:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 30)
p2 = Person("Alice", 30)

print(p1 == p2) # False
```

As these are custom objects, `==` won't check the values inside them. To check the equality of custom objects, we need to override the `__eq__` method.

For custom objects, we can define our own equality logic by overriding the `__eq__` method:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
p3 = Person("Bob", 25)

print(p1 == p2)  # True
print(p1 == p3)  # False
```

In this example, two `Person` objects are considered equal if their `name` and `age` attributes are equal.

#### Potential Interview Questions

1. **What is the difference between `==` and `is` in Python?**
   - `==` checks for value equality, meaning it compares the values of two objects to see if they are the same.
   - `is` checks for identity, meaning it compares the memory addresses of two objects to see if they are the same object.

2. **How would you implement a custom equality method for a class?**
   - By overriding the `__eq__` method, we can define our own logic for comparing the values of custom objects.

3. **Why should you override `__hash__` when you override `__eq__`?**
   - In Python, objects that compare equal must have the same hash value if they are to be used as dictionary keys or stored in sets. Therefore, when you override `__eq__`, you should also override `__hash__` to maintain consistency.

4. **How do you ensure that the `__eq__` method only compares objects of the same class?**
   - Use the `isinstance` function to check if the other object is an instance of the same class before comparing attributes.

#### Additional Examples and Tips

1. **Comparing Nested Objects**:
   - If a class has attributes that are instances of other classes, you need to ensure that their equality methods are also defined.

    ```python
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
    ```

2. **Implementing `__hash__`**:
   - Ensure objects that compare equal also have the same hash value.

    ```python
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

    print(len(people))  # 1, because p1 and p2 are considered equal
    ```

3. **Comparing Different Attributes**:
   - Customize the comparison to check specific attributes or a combination of attributes based on the requirements.

    ```python
    class Employee:
        def __init__(self, emp_id, name, company):
            self.emp_id = emp_id
            self.name = name
            self.company = company

        def __eq__(self, other):
            if isinstance(other, Employee):
                return (self.emp_id, self.name, self.company) == (other.emp_id, other.name, other.company)
            return False

    emp1 = Employee(1, "Alice", "CompanyA")
    emp2 = Employee(1, "Alice", "CompanyA")

    print(emp1 == emp2)  # True
    ```

### Summary

Understanding how to compare objects in Python is fundamental for OOP interviews. By implementing custom equality methods, you can ensure that your objects behave as expected when compared. Practice with various examples and scenarios to solidify your understanding.

---