from collections import deque

N,M = map(int,input().split())
grid = [list(input()) for _ in range(N)]
dir = [(0,1),(0,-1),(1,0),(-1,0)]
sum = 0
visited = [[False]*M for _ in range(N)]

def bfs(x,y,grid,N,M):
    queue = deque([(x,y)])
    visited[x][y] = True
    count = 0

    while queue:
      x,y = queue.popleft()

      if grid[x][y] == 'P':
        count += 1

      for dx, dy in dir:
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and grid[nx][ny] != 'X':
          visited[nx][ny] = True
          queue.append((nx,ny))

    return count

for i in range(N):
  for j in range(M):
    if not visited[i][j] and grid[i][j] == 'I':
      sum = bfs(i,j,grid,N,M)
      break
if sum == 0:
  print('TT')
else:
  print(sum)