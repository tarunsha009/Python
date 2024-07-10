In Python, we have :

**List Comprehension:**
 It returns the list
```python
list1 = [1,2,3,4]
result = [ x **2 for x in list1]
```

**Generator Function:**
It returns the tuple
```python
list1 = [1,2,3,4]
gen = ( x **2 for x in list1)
```

**Dictionary Comprehension:**
It returns the dictionary

```python
squares = {x: x**2 for x in range(6)}
print(squares)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

```

so for all the above, bracket type changes but the internal logic are mostly same.