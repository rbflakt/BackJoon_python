from collections import defaultdict,deque

def find():
  T = int(input())
  result = []
  
  for _ in range(T):
     graph = defaultdict(list)
     N,M = map(int,input().split())
     for _ in range(M):
       a,b = map(int,input().split())
       graph[a].append(b)
       graph[b].append(a)
    
     visited = set()
     queue = deque([1])
     visited.add(1)
     node_min = 0

     while queue:
       node = queue.popleft()
       for i in graph[node]:
         if i not in visited:
           visited.add(i)
           queue.append(i)
           node_min += 1
     result.append(node_min)

  for _ in result:
    print(_)

find()