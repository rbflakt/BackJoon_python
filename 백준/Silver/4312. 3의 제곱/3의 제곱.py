import sys
input = lambda: sys.stdin.readline().strip()
ini = lambda: int(input())
ins = lambda: [*map(int, input().split())]
inf = float('inf')

while N := ini():
    N -= 1
    A = []
    i = 0
    while 1<<i <= N:
        if N&(1<<i):
            A.append(3**i)
        i += 1
    if A:
        print("{ " + ", ".join(map(str, A)) + " }")
    else:
        print("{ }")