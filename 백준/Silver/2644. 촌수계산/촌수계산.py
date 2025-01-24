from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = {}
visited = [0] * (n+1)
dist = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    if x in graph.keys():
        graph[x].append(y)
    else:
        graph[x] = [y]
    if y in graph.keys():
        graph[y].append(x)
    else:
        graph[y] = [x]

queue = deque([a])

while queue:
    tmp = queue.pop()
    
    for i in graph[tmp]:
        if not visited[i]:
            visited[i] = 1
            queue.appendleft(i)
            dist[i] = dist[tmp] + 1

if dist[b] == 0:
    print(-1)
else:
    print(dist[b])