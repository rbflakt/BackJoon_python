from collections import deque 

N,M = map(int,input().split())
a = list(map(int,input().split()))

known = [0] * (N + 1)

for i in range(1, a[0]+1):
    known[a[i]] = 1

parties = []

graph = [[] for i in range(N+1)]

for i in range(M):
    b = list(map(int,input().split()))
    parties.append(b) 

    for j in b[1:]:
        for i in b[1:]:
            if j!=i:
                graph[j].append(i)


def bfs(graph, party, known):
    flag = False
    queue = deque([party[1]])
    visited = [0] * (N+1)
    while queue:
        v = queue.pop()
        if known[v] == 1:
            flag = True
            break
        if not visited[v]:
            visited[v] = 1
            for i in graph[v]:
                queue.appendleft(i)
                if known[i] == 1:
                    flag = True
                    break
    return flag
                
ans = 0
for party in parties:
    if not bfs(graph, party, known):
        ans += 1
        
print(ans)