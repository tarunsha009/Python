def print_name(name, count):
    if count == 5:
        return
    print(f'Hi, {name}')
    count += 1
    print_name(name, count)


def print_one_to_n(n):
    if n == 0:
        return
    print_one_to_n(n - 1)
    print(n)

def print_one_to_n_opposite(n):
    if n == 0:
        return
    print(n)
    print_one_to_n_opposite(n - 1)


def factorail_function(n):
    if n == 1:
        return 1
    return n * factorail_function(n - 1)

def factorail_function2(n , total):
    if n == 1:
        return total
    return factorail_function2(n - 1, total * n)

print_name('PyCharm', 1)
print("####################")
print_one_to_n(10)
print("####################")
print_one_to_n_opposite(10)
print("####################")
print(factorail_function(5))
print("####################")
print(factorail_function2(5, 1))