N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]  # N by N 정사각형 물의 양
transform = [list(map(int, input().split())) for _ in range(M)]  # M개의 명령어, [di, si]

dx=[-1,-1,1,1]
dy=[-1,1,-1,1]
# 대각선 및 8방향 이동을 위한 dx, dy (1번부터 8번까지 순서대로: 좌, 좌상단, 위, 우상단, 우, 우하단, 아래, 좌하단)
move_dx = [0, -1, -1, -1, 0, 1, 1, 1]  # 순서대로 좌, 좌상단, 위, 우상단, 우, 우하단, 아래, 좌하단
move_dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 초기 구름 위치 (N, 1), (N, 2), (N-1, 1), (N-1, 2)
rain = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

# 구름 이동 및 물 증가 함수
def move_cloud_and_rain(rain, di, si):
    new_rain = []
    visited = [[False] * N for _ in range(N)]  # 구름이 있던 자리를 기록
    
    # 구름 이동
    for x, y in rain:
        nx = (x + move_dx[di - 1] * si) % N  # di는 1부터 시작하므로 배열 인덱스를 맞추기 위해 -1
        ny = (y + move_dy[di - 1] * si) % N
        new_rain.append((nx, ny))
        visited[nx][ny] = True  # 구름이 멈춘 자리 표시
        grid[nx][ny] += 1  # 물의 양 증가
    
    # 대각선에 물이 있을 경우 물 증가 (좌상단, 우상단, 좌하단, 우하단)
    for x, y in new_rain:
        count = 0
        for d in range(4):  # 4방향 대각선
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] > 0:
                count += 1
        grid[x][y] += count  # 대각선에 물이 있으면 그 수만큼 물 증가

    # 새로운 구름 생성
    rain = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and grid[i][j] >= 2:  # 구름이 없고 물의 양이 2 이상인 곳에 구름 생성
                rain.append((i, j))
                grid[i][j] -= 2  # 물의 양 2 감소

    return rain

# 명령어에 따라 구름 이동과 물 증가 시뮬레이션
for di, si in transform:
    rain = move_cloud_and_rain(rain, di, si)

# 최종 물의 양의 합 출력
total_water = sum(sum(row) for row in grid)
print(total_water)