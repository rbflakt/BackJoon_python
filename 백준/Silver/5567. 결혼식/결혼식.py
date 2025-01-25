from collections import deque

# BFS 함수: 1번 사람의 친구와 친구의 친구들을 찾아 리스트에 저장
def friends(graph, start):
    visited = [False] * (len(graph)+1)  # 그래프 길이만큼 false값 할당
    queue = deque([start])  # 1번 사람부터 시작(초기화)
    visited[start] = True  # 1번 사람 방문 처리
    friends_list = []  # 친구와 친구의 친구를 저장할 리스트
    level = 0 #친구의 관계 레벨(친구-친구인지, 1의친구인지 여부)

    while queue:
        current_level_size = len(queue)  # 현재 레벨의 노드 수
        level += 1  #for문을 돌고 친구의 친구 탐색
				
        for _ in range(current_level_size):
            current = queue.popleft()  # 현재 노드 꺼냄

            for neighbor in graph[current]:  # 현재 노드의 이웃들 순회
                if not visited[neighbor]:  # 방문하지 않은 이웃 노드일 때(false일때)
                    visited[neighbor] = True  # 방문 처리
                    queue.append(neighbor)  # 큐에 추가
                    if level <= 2:  # 1번 사람의 친구와 친구의 친구까지만 리스트에 추가
                        friends_list.append(neighbor)

        if level == 2:  # 친구의 친구까지만 탐색, for문을 다 돌고 난 후에 실행
            break

    return len(friends_list)

# 입력 처리
n = int(input())  # 사람의 수
m = int(input())  # 관계의 수

# 그래프 초기화(리스트가 속도 더 빠름)
graph = {i: [] for i in range(1, n + 1)}

# 관계 입력 처리
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# BFS 실행: 1번 사람의 친구와 친구의 친구 찾기
friends_of_friends = friends(graph, 1)

# 결과 출력
print(friends_of_friends)