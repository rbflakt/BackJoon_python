T = int(input())
dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def find():
  M,N,K = map(int,input().split())
  info = [list(map(int,input().split())) for _ in range(K)]
  visited = [[False]*N for _ in range(M)]
  grid = [[0]*N for _ in range(M)]
  for x1,y1 in info:
    grid[x1][y1] = 1 #배추 위치 넣기
  
  ###input###

  def dfs(x,y):
    stack = [(x,y)]
    visited[x][y] = True

    while stack:
      x,y = stack.pop()
      for dx,dy in dir:
        nx,ny = dx+x,dy+y
        if 0<=nx<M and 0<=ny<N and not visited[nx][ny] and grid[nx][ny] == 1:
          stack.append((nx,ny))
          visited[nx][ny] = True
  
  count = 0
  for i in range(M):
    for j in range(N):
      if grid[i][j] == 1 and not visited[i][j]:
        dfs(i,j)
        count += 1
  return count
result = [find() for _ in range(T)]
print(*result)