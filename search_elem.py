def search(arr, N, X):
    for i in range(N):
        if arr[i] == X:
            return i
    return -1

arr = [1, 3, 5, 33, 32]
n = len(arr)
x = int(input('Enter element for search: '))
print(search(arr, n, x))