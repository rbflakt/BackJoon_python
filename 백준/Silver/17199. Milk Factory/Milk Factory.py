N = int(input())

factory = [[0] * (N+1) for _ in range(N+1)]

for _ in range(N - 1):
    f1, f2 = map(int, input().split())
    factory[f1][f2] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if factory[i][k] == 1 and factory[k][j] == 1:
                factory[i][j] = 1

ans = -1
for i in range(1, N + 1):
    count = 0
    for j in range(1, N + 1):
        if factory[j][i] == 1:  # i로 갈 수 있는 모든 노드 체크
            count += 1

    if count == N - 1:
        ans = i
        break

print(ans)