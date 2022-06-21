def cred(credit, r, mr):
    n = 1
    sum_p0 = 0
    while n <= 12:
        p0 = credit*mr/100
        sum_p0 += p0
        print(round(p0, 2))
        ub0 = credit - p0
        print(round(ub0, 2))
        ub1 = ub0 + r*ub0/1200
        print(round(ub1, 2))
        credit = ub1
        n += 1
    print(round(sum_p0, 2))
    return ub1



credit = int(input("What is the spending(5000): "))
r= int(input("Yearly card interest rate is(18): "))
mr = int(input("Min Monthly rate to be paid per month(2): "))
balance = cred(credit, r, mr)
print(round(balance, 2))