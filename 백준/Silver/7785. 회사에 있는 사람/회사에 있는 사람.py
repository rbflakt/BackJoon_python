import sys
input = sys.stdin.readline
n = int(input())
people_dict = dict(input().split() for _ in range(n))
result = []

for a,b in people_dict.items():
  if b != "leave":
    result.append(a)

result.sort(reverse=True)
print(*result)