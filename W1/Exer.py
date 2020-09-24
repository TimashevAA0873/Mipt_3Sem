a = int(input())
b = 0
for i in range(1, a, 1):
    b = float(pow(i, 0.5) ** 2)
    if i == b:
        print(i, '/n')
