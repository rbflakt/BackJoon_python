import heapq

def change(grid,n):
  directions=[(0,1),(1,0),(0,-1),(-1,0)] #오른쪽, 아래, 왼쪽, 위
  costs=[[float('inf')]*n for _ in range(n)]
  costs[0][0]=0

  min_heap=[(0,0,0)]

  while min_heap:
    current_cost,x,y=heapq.heappop(min_heap)
    if (x,y)==(n-1,n-1):
      return current_cost
    if current_cost>costs[x][y]:
      continue
    for dx,dy in directions:
      nx,ny=x+dx,y+dy

      if 0<=nx<n and 0<=ny<n:
        next_cost=current_cost+(1 if grid[nx][ny]=='0' else 0)

        if next_cost<costs[nx][ny]:
          costs[nx][ny]=next_cost
          heapq.heappush(min_heap,(next_cost,nx,ny))
  return -1

n=int(input())
grid=[input().strip() for _ in range(n)]

#result=change(grid,n)
print(f"{change(grid,n)}")