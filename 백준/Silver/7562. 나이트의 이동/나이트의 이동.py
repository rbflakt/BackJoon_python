import heapq

T = int(input())
dir = [(-2,1),(-1,2),(1,2),(2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
def find():
  n = int(input())
  info = [list(map(int,input().split())) for _ in range(2)]
  cost = [[float('inf')]*n for _ in range(n)]
  #visited = [[False]*n for _ in range(n)]

  min_heap = [(0,info[0][0],info[0][1])]
  cost[info[0][0]][info[0][1]] = 0

  def bfs():
     while min_heap:
      current_cost,x,y = heapq.heappop(min_heap)
      if current_cost > cost[x][y]:
        continue
      if x == info[1][0] and y == info[1][1]:
        return cost[x][y]
      for dx,dy in dir:
        nx,ny = dx+x,dy+y
        if 0<=nx<n and 0<=ny<n:
          next_cost = current_cost + 1
          #print(next_cost)
          if next_cost < cost[nx][ny]:
            cost[nx][ny] = next_cost
            heapq.heappush(min_heap,(next_cost,nx,ny))
  return bfs()

for _ in range(T):
  print(find())