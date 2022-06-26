def get_min_bal(bal, r):
    min_pay = 10
    org_bal = bal
    while bal > 0:
        bal = org_bal
        for i in range(12):
            b0 = bal - min_pay
            bal = b0*r/12 + b0
        min_pay += 10
    return min_pay - 10

# x = 3329
# r = .20
x = int(input("Initial debt: "))
r = float(input("Rate of interest: "))
installment = get_min_bal(x, r)
print("Lowest payment", installment)