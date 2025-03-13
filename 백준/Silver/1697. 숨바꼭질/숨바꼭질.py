import heapq

def find():
  N,K = map(int,input().split())
  #dir = [1,-1,2]
  graph = [float('inf')]*100001

  def bfs():
    min_heap = [(0,N)] #현재 흐른 시간(cost),수빈의 위치
    graph[N] = 0
    while min_heap:
      current_cost,x = heapq.heappop(min_heap)
      if current_cost > graph[x]:
        continue
      if x == K:
        return current_cost
      for na in (x-1,x+1,x*2):
        if 0<=na<=100000:
          next_cost = current_cost + 1
          if next_cost < graph[na]:
            graph[na] = next_cost
            heapq.heappush(min_heap,(next_cost,na))
            #print(graph[na],na)

  return bfs()

print(find())