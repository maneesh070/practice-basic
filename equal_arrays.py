def check(A, B, n):
    if len(A) != len(B):
        return 0
    i = 0
    while i < n:
        if A[i] in B:
            i += 1
        else:
            return 0
    return 1

a = [1,2,3,3]
b = [2,3,1,1]
n = len(a)
print(check(a,b,n))