T = int(input())
for _ in range(T):
    a = int(input())
    for unit in [25, 10, 5, 1]:
        print(a // unit)
        a %= unit