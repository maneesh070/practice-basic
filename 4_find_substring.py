def strstr(s,x):
    if x in s:
        return 1
    return 0
s = 'Geeksforgeeks'
x = 'forgeek'
a = strstr(s,x)
print(a)