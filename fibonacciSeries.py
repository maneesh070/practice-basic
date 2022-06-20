def feb(x):
    if x == 0 or x == 1:
        return 1
    else:
        return feb(x - 1) + feb(x - 2)

x = int(input("Enter integer from where to start: "))
fibseries = feb(x)
print(fibseries)