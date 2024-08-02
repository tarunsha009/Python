

def simplifyPath(path: str):
    stack = []
    abc = path.split('/')
    for i in abc:
        if i == '..' and len(stack) >=1:
            stack.pop()
        elif i != '' and i != '..' and i !='.':
            stack.append("/"+ i)

    return str("".join(stack)) if len(stack) >= 1 else "/"



path = "/home/"
print(simplifyPath(path))
print(simplifyPath("/home//foo/"))
print(simplifyPath("/home/user/Documents/../Pictures"))
print(simplifyPath("/../"))
print(simplifyPath("/.../a/../b/c/../d/./"))

abc = []
# s = "leEeetcode"
# s = "abBAcC"
s = "s"
for i in s:
    if abc:
        if i.islower() and abc[-1].isupper() and i.upper() == abc[-1].upper():
            abc.pop()
        elif i.isupper() and abc[-1].islower() and i.upper() == abc[-1].upper():
            abc.pop()
        else:
            abc.append(i)
    else:
        abc.append(i)


print(abc)
