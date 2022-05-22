def findTriplets(arr,n):
    for i in range(n):
        for  j in range(n):
            if i != j:
                for k in range(n):
                    if i != k and k!=j:
                        if arr[i] + arr[j]+arr[k] == 0:
                            return 1
    return 0

arr = [10, 2, 4, 6, 5, 0]
n = len(arr)
triplet = findTriplets(arr, n)
print(triplet)