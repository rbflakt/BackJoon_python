import sys
input = sys.stdin.readline
N, M = map(int, input().split())
password_dict = dict(input().split() for _ in range(N))
for _ in range(M):
    print(password_dict[input().strip()])