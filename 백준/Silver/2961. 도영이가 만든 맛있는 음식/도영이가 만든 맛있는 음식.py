from itertools import combinations

N = int(input())
sour = []
bitter = []

for _ in range(N):
    a, b = map(int, input().split())
    sour.append(a)
    bitter.append(b)

min_diff = float('inf')

for i in range(1, N+1):
    for c in combinations(range(N), i):
        total_sour = 1
        total_bitter = 0
        for idx in c:
            total_sour *= sour[idx]
            total_bitter += bitter[idx]
        diff = abs(total_sour - total_bitter)
        min_diff = min(min_diff, diff)

print(min_diff)