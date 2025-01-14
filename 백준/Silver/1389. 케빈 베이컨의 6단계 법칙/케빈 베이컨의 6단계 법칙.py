N, M = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    from collections import deque

def bfs(graph, start, n):
    distances = [-1] * (n + 1)
    distances[start] = 0
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    
    return distances

def calculate_all_distances(graph, n):
    min_distance_sum = float('inf')
    min_nodes = []
    
    for i in range(1, n + 1):
        distances = bfs(graph, i, n)
        total_distance = sum(d for d in distances if d != -1)
        
        if total_distance < min_distance_sum:
            min_distance_sum = total_distance
            min_nodes = [i]
        elif total_distance == min_distance_sum:
            min_nodes.append(i)
    
    return min_nodes

min_nodes = calculate_all_distances(graph, N)

print(min(min_nodes))