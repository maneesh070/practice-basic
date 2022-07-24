def product(arr, n, mod):
    product = 1
    for i in range(n):
        product = ((product%mod)*(arr[i])%mod)%mod

    return product



arr = [1,2,3,4]
n = len(arr)
modulo = (10**9) + 7
#modulo: (a*b)%m = ((a%m)*(b%m))%m
print(product(arr, n, modulo))