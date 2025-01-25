import sys
sys.setrecursionlimit(10**6)

R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

def solution(grid):
    visited = [[False for _ in range(C)] for _ in range(R)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    total_o, total_v = 0, 0

    def dfs(x, y):
        stack = [(x, y)]
        v_count, o_count = 0, 0

        while stack:
            cx, cy = stack.pop()
            if visited[cx][cy]:
                continue
            visited[cx][cy] = True

            if grid[cx][cy] == 'o':
                o_count += 1
            elif grid[cx][cy] == 'v':
                v_count += 1

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and grid[nx][ny] != '#':
                    stack.append((nx, ny))

        return o_count, v_count

    for i in range(R):
        for j in range(C):
            if not visited[i][j] and (grid[i][j] == 'o' or grid[i][j] == 'v'):
                o_count, v_count = dfs(i, j)
                if o_count > v_count:
                    total_o += o_count
                else:
                    total_v += v_count

    return total_o, total_v

total_o, total_v = solution(grid)
print(total_o, total_v)