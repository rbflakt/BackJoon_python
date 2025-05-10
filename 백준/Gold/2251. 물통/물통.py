A, B, C = map(int, input().split())
result = set()

visited = [[False] * (B + 1) for _ in range(A + 1)]

def dfs(a, b, c):
    if visited[a][b]:
        return
    visited[a][b] = True

    if a == 0:
        result.add(c)

    for from_i, to_i in [(0,1), (0,2), (1,0), (1,2), (2,0), (2,1)]:
        next_state = [a, b, c]
        from_l = next_state[from_i] #붓는쪽 물의 양
        to_l = next_state[to_i] #받는쪽 물의 양
        to_cap = [A, B, C][to_i] #받는쪽의 최대용량(인풋으로 받았던 값)

        move = min(from_l, to_cap - to_l) #붓는쪽 물의양과 (수용가능한 최댓값 - 받는쪽 기존에 있던 물의 양) 중 최소를 고름
        next_state[from_i] -= move
        next_state[to_i] += move

        dfs(next_state[0], next_state[1], next_state[2])

dfs(0, 0, C)

print(" ".join(map(str, sorted(result))))