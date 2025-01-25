from collections import deque

N, M = map(int, input().split())

graph = {}
dist = [0] * (N+1)
visited = [0] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    if x in graph.keys():
        graph[x].append(y)
    else:
        graph[x] = [y]
    if y in graph.keys():
        graph[y].append(x)
    else:
        graph[y] = [x]

queue = deque([1])

while queue:
    tmp = queue.pop()
    
    if not visited[tmp]:
        visited[tmp] = 1
        for i in graph[tmp]:
            queue.appendleft(i)
            if not dist[i] and not visited[i]:
                dist[i] = dist[tmp] + 1

max = 0
cnt = 0
for i in range(1, N+1):
    if dist[i] > dist[max]:
        max = i
        cnt = 1
    elif dist[i] == dist[max]:
        cnt += 1

print(f"{max} {dist[max]} {cnt}")