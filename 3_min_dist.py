def minDest(arr, n, x, y):
    if x not in arr or y not in arr:
        return -1
    # else:
    #     b = [i for i in range(n) if arr[i]==x]
    #     c = [i for i in range(n) if arr[i]==y]
    #     f = []
    #     for i in c:
    #         for j in b:
    #             f.append(abs(i-j))

    #     return min(f)

    l = -1
    r = -1
    m = n
    diff = m
    for i in range(n):
        if arr[i] == x:
            l = i
        if arr[i] == y:
            r = i
        if l>0 and r>0:
            diff = abs(l-r)
        m = min(diff, m)
    return m

a = [13, 98, 5, 10, 23, 13, 4, 53, 60, 78, 66, 68, 44, 69, 79, 71, 90, 17, 91, 84, 34, 52, 12, 11, 57, 61, 2]
n = len(a)
x = int(input('Enter integer 1(78): '))
y = int(input('Enter integer 2(68): '))
distMin = minDest(a, n, x, y)
print(distMin)