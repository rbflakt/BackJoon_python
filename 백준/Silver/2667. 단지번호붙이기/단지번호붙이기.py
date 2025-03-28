N = int(input())
arr = [list(map(int, list(input().strip()))) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
dir = [(0,1),(1,0),(0,-1),(-1,0)]
result = []

def dfs(x,y):
  stack = [(x,y)]
  visited[x][y] = True
  area = 1
  while stack:
    dx,dy = stack.pop()
    for a,b in dir:
      nx,ny = dx+a,dy+b
      if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and arr[nx][ny] == 1 :
        stack.append((nx,ny))
        visited[nx][ny] = True
        area += 1
  result.append(area)

for i in range(N):
  for j in range(N):
    if not visited[i][j] and arr[i][j] == 1:
      dfs(i,j)

result.sort()
print(len(result))
for k in result:
  print(k)