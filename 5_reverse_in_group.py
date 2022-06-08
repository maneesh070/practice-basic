# Only applicable when N%K == 0
def reverseInGroup(arr, N, K):
    x = 0
    j = 0
    n = 1
    a = []
    while j < N:
        l = 0
        for i in range(x, n*K):
            a.append(arr[n*K-1-l])
            j += 1
            l += 1
        n += 1
        x = j
    return a


arr = [1, 2, 3, 4, 5, 6]
N = len(arr)
K = int(input("Enter your key element: "))
reversedArr = reverseInGroup(arr, N, K)
print(reversedArr)