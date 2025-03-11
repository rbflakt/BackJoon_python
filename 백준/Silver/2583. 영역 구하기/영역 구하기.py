M, N, K = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(K)]
grid = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]
dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

for x1, y1, x2, y2 in info:
    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] = 1  # 벽 표시

def dfs(x, y):
    stack = [(x, y)]
    visited[x][y] = True
    area = 1 

    while stack:
        cx, cy = stack.pop()
        for dx, dy in dir:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                stack.append((nx, ny))
                area += 1

    return area

count = 0
result = []

for i in range(M):
    for j in range(N):
        if grid[i][j] == 0 and not visited[i][j]:
            count += 1
            result.append(dfs(i, j))


print(count)
print(*sorted(result)) 