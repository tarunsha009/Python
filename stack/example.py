def backspaceCompare(s: str, t: str) -> bool:
    stack1 = []
    stack2 = []
    for i in s:
        if stack1 and i == '#':
            stack1.pop()
        else:
            stack1.append(i)

    for j in t:
        if stack2 and j == '#':
            stack2.pop()
        else:
            stack2.append(j)

    return stack1 == stack2


s = "y#fo##f"
t = "y#f#o##f"
backspaceCompare(s,t)