def thirdLargest(arr, n):
        iteration = 0
        new_list = []
        j = 0
        while iteration < n:
            maximum = float('-inf')
            for i in range(n - iteration):
                if arr[i] > maximum:
                    maximum = arr[i]
                    j = i
            arr.pop(j)
            new_list.append(maximum)
            iteration += 1
        if n < 3:
            return -1
        return new_list[2]
arr = [1,3]
n = len(arr)
print(thirdLargest(arr, n))