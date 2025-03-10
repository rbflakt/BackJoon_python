import heapq

N,M = map(int,input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]

def bfs(grid,N,M):
  dir = [(0,1),(1,0),(-1,0),(0,-1)]
  costs = [[float('inf')] * M for _ in range(N)]
  costs[0][0] = 1

  min_heap = [(1,0,0)] #cost,x,y
  while min_heap:
    current_cost,x,y = heapq.heappop(min_heap)
    if (x,y) == (N-1,M-1):
      return current_cost
    if current_cost > costs[x][y]:
      continue
    for dx,dy in dir:
      nx,ny = dx+x,dy+y
      if 0<=nx<N and 0<=ny<M and grid[nx][ny] == 1:
          next_cost = current_cost + 1
          #print("바뀌기전 next:",next_cost)
          if next_cost < costs[nx][ny]:
            costs[nx][ny] = next_cost
            heapq.heappush(min_heap,(next_cost,nx,ny))
          #heapq.heappush(min_heap,(next_cost,nx,ny))

result = bfs(grid,N,M)
print(result)