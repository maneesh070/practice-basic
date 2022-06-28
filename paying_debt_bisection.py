balance = 320000
annualInterestRate = 0.20

def pay_debt_bisection(balance, annualInterestRate):
    min_payment = balance/12
    max_payment = (balance*(1 + annualInterestRate/12)**12)/12
    avg_pay = (min_payment + max_payment)/2
    while True:
        bal = balance
        for month in range(12):
            bal = bal - avg_pay
            bal = bal*annualInterestRate/12 + bal

        if -0.01 <= bal and bal <= 0.01:
            return round(avg_pay, 2)
        elif bal > 0:
            min_payment = avg_pay
            avg_pay = (min_payment + max_payment)/2
        elif bal < 0:
            max_payment = avg_pay
            avg_pay = (min_payment + max_payment)/2

min_pay = pay_debt_bisection(balance, annualInterestRate)
print(min_pay)