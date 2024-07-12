### Session 10: Exception Handling

In this session, we will focus on understanding and practicing exception handling in Python. Exception handling is a crucial part of writing robust and error-free code. We'll start with the basics and gradually move on to more advanced concepts.

#### Topics to Cover:
1. **Basic Exception Handling**
2. **Catching Multiple Exceptions**
3. **The `else` and `finally` Clauses**
4. **Custom Exceptions**
5. **Exception Handling in Functions**

### Basic Exception Handling

The basic structure of exception handling in Python uses the `try` and `except` blocks. Here's a simple example:

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("Cannot divide by zero!")
```

### Catching Multiple Exceptions

You can catch multiple exceptions by specifying them in a tuple:

```python
try:
    result = 10 / 0
except (ZeroDivisionError, TypeError):
    print("An error occurred!")
```

### The `else` and `finally` Clauses

The `else` clause executes if no exceptions were raised, and the `finally` clause executes regardless of whether an exception was raised or not:

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("The division was successful!")
finally:
    print("This will always execute.")
```

### Custom Exceptions

You can define your own exceptions by creating a new class that inherits from the `Exception` class:

```python
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error!")
except CustomError as e:
    print(e)
```

### Exception Handling in Functions

You can handle exceptions within functions or propagate them to the caller using the `raise` statement:

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        raise

try:
    divide(10, 0)
except ZeroDivisionError:
    print("Handled in the caller.")
```