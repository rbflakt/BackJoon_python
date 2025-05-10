import sys
input = sys.stdin.read

data = input().split()
N = int(data[0])
arr = [list(map(int, data[i*N + 1 : (i+1)*N + 1])) for i in range(N)]

psum = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        psum[i][j] = (
            arr[i-1][j-1]
            + psum[i-1][j]
            + psum[i][j-1]
            - psum[i-1][j-1]
        )

max_profit = -float('inf')

for k in range(1, N+1):  # K
    for i in range(k, N+1):
        for j in range(k, N+1):
            total = (
                psum[i][j]
                - psum[i-k][j]
                - psum[i][j-k]
                + psum[i-k][j-k]
            )
            max_profit = max(max_profit, total)

print(max_profit)