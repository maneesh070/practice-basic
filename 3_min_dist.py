def minDest(arr, n, x, y):
    if x not in arr or y not in arr:
        return -1
    c = 10000
    for  i in range(n):
        if arr[i]==x:
            for j in range(n):
                if arr[j] == y:
                    if abs(i-j)<c:
                        c= abs(i-j)
    return c

a = [13, 98, 5, 10, 23, 13, 4, 53, 60, 78, 66, 68, 44, 69, 79, 71, 90, 17, 91, 84, 34, 52, 12, 11, 57, 61, 2]
n = len(a)
x = int(input('Enter integer 1(78): '))
y = int(input('Enter integer 2(68): '))
distMin = minDest(a, n, x, y)
print(distMin)