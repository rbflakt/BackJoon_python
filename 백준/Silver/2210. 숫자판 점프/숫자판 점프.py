arr = [list(map(int, input().split())) for _ in range(5)]
dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
result = set() #중복제거

def dfs(x, y, path):
    if len(path) == 6:
        result.add(tuple(path))
        return

    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, path + [arr[nx][ny]])

for i in range(5):
    for j in range(5):
        dfs(i, j, [arr[i][j]])

print(len(result))
#print(result)