

x = 0
y = 1
z = 0
n = 30
a = 10000
for i in range(n):
    s = x + y
    x = y
    y = s

    print(s)

    if s >= a:
        print(f"Сумма должна быть не более {a}")
        break