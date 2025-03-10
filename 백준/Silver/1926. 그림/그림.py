n,m = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dir1 = [(0,1),(1,0),(-1,0),(0,-1)]
#dir2 = [(-1,1),(1,-1),(-1,-1),(1,1)]
def find(graph):
  count = 0
  visited = [[False]*m for _ in range(n)]
  result = []
  def dfs(x,y):
    stack = [(x,y)]
    visited[x][y] = True
    area = 1
    while stack:
      cx, cy = stack.pop()
      neighbors = [(cx + dx, cy + dy) for dx, dy in dir1]  # 상하좌우 위치 계산
      isolated = all(0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 for nx, ny in neighbors if 0 <= nx < n and 0 <= ny < m)
      for dx,dy in dir1:
        nx,ny = dx+cx,dy+cy
        if 0 <= nx < n and 0<= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
            stack.append((nx,ny))
            visited[nx][ny] = True
            area += 1
        if isolated:
          result.append(area)
          return
    result.append(area)

  for i in range(n):
    for j in range(m):
      if not visited[i][j] and graph[i][j] == 1:
        dfs(i,j)
        count += 1
  if not result:
    return count,0
  return count,max(result)
a,b = find(graph)
print(a,b)