def bank(x, y):
    for i in range(y):
        x = x + (x/10)
    return x


print(bank(2023, 3))
