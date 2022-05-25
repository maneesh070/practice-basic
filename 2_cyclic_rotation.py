def rotate(arr, n):
    a = []
    a.append(arr[n-1])
    for i in range(0, n-1):
        a.append(arr[i])
    return a

arr = [1,2,3,4,5]
n = len(arr)
reverseStr = rotate(arr, n)
print(reverseStr)