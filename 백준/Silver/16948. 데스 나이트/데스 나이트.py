import heapq

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
dir = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

def bfs():
    cost = [[float('inf')] * N for _ in range(N)]
    cost[r1][c1] = 0
    min_heap = [(0, r1, c1)]

    while min_heap:
        current_cost, x, y = heapq.heappop(min_heap)
        if (x, y) == (r2, c2):
            return current_cost
        if current_cost > cost[x][y]:
            continue
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                next_cost = current_cost + 1
                if next_cost < cost[nx][ny]:
                    cost[nx][ny] = next_cost
                    heapq.heappush(min_heap, (next_cost, nx, ny))

    return -1

result = bfs()
print(result)