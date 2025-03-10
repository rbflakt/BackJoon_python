n,m = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dir1 = [(0,1),(1,0),(-1,0),(0,-1)]
dir2 = [(-1,1),(1,-1),(-1,-1),(1,1)]
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
      #if visited[cx][cy]:
        #continue
      #visited[cx][cy] = True 이부분 때문에 생각해줘야하는 영역이 전부 패스됨.
      for dx,dy in dir1:
        nx,ny = dx+cx,dy+cy
        if 0 <= nx < n and 0<= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
          stack.append((nx,ny))
          visited[nx][ny] = True
          area += 1
      for dx,dy in dir2:
        #if 0 <= nx < n and 0<= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
          #count += 1
          #area += 1
          #stack.append((nx,ny))
        if 0 <= nx < n and 0<= ny < m and not visited[nx][ny] and graph[nx][ny] == 0:
          result.append(area)
    result.append(area)
  for i in range(n):
    for j in range(m):
      if not visited[i][j] and graph[i][j] == 1:
        count += 1
        dfs(i,j)
  if not result:
     return count,0
  return count,max(result)
a,b = find(graph)
print(a,b)