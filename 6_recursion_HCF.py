
def gcdRecur(a, b):
    if b == 0:
        return a
    elif a > b:
        q = a//b
        r = a%b
        if r == 0:
            return b
        else:
            a = b
            b = r
            return gcdRecur(a, b)
    elif a < b:
        q = b//a
        r = b%a
        if r == 0:
            return a
        else:
            b = a
            a = r
            return gcdRecur(a, b)

a = int(input("Enter any integer: "))
b = int(input("Enter second integer: "))
hcf = gcdRecur(a, b)
print(hcf)