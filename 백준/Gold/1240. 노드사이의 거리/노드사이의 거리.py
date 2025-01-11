from collections import defaultdict

N,M = map(int,input().split())
graph = defaultdict(list)

for _ in range(N-1):
  u,v,d = map(int,input().split())
  graph[u].append((v,d))
  graph[v].append((u,d))

def find(s,e):
  visited = set()
  stack = [(s,0)]

  while stack:
    current,cost = stack.pop()

    if current in visited:
      continue
    visited.add(current)

    if current == e:
      return cost

    for next,next_cost in graph[current]:
      if next not in visited:
        stack.append((next,next_cost+cost))

for _ in range(M):
    s,e = map(int,input().split())
    find(s,e)
    print(find(s,e))