def thirdLargest(arr, n):
        first_largest = float('-inf')
        second_largest = float('-inf')
        third_largest = float('-inf')
        if n < 3:
            return -1
        else:
            for i in range(n):
                if arr[i] >= first_largest:
                    third_largest = second_largest
                    second_largest = first_largest
                    first_largest = arr[i]
                elif arr[i] >= second_largest and arr[i] < first_largest:
                    third_largest = second_largest
                    second_largest = arr[i]
                elif arr[i] >= third_largest and arr[i] < second_largest:
                    third_largest = arr[i]
        return third_largest


arr = [1,3, 5, 7,5, 5]
n = len(arr)
print(thirdLargest(arr, n))