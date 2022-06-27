def rem_bal_aftr_12_mnths(bal, r, pay):
        for i in range(12):
            bal = bal - pay
            bal = bal*r + bal
        return bal

def min_pay(balance, rate):
    r = rate/12
    min_pay  = 10
    while rem_bal_aftr_12_mnths(balance, r, min_pay) > 0:
        min_pay += 10
    return min_pay


bal = int(input("Enter principal value: "))
annual_rate = 0.2
min_pay = min_pay(bal,annual_rate)
print(f'Lowest payment: {min_pay}')