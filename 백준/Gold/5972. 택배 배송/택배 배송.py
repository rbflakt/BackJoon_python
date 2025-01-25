import heapq #우선순위 큐를 구현하기 위해 사용

def find(N,graph): #소 먹이의 최솟값을 찾기위한 함수
  distances=[float('inf')]*(N+1) #거리 배열 무한대 초기화(inf이용)
  distances[1]=0 #시작점은 1번째 노드

  pq=[(0,1)] #(현재 가중치, 현재 노드)

  while pq:
    sum,current_node=heapq.heappop(pq) #현재 가장 짧은 거리의 노드를 큐에서 꺼냄!
    if distances[current_node]<sum: #이미 최단경로이면 유지
      continue
    for neighbor,weight in graph[current_node]: #현재 노드와 연결된 이웃노드 확인
      distance = sum + weight

      if distance < distances[neighbor]: #새로운 경로가 더 짧다면, 경로 갱신 후 큐에 추가
        distances[neighbor] = distance
        heapq.heappush(pq, (distance, neighbor))

  return distances[N] #N까지 최단거리 반

N,M=map(int,input().split())

graph=[[] for _ in range(N+1)] #인접리스트 초기화(1부터 N까지)

for _ in range(M):
  u,v,w=map(int,input().split())
  graph[u].append((v,w))
  graph[v].append((u,w)) #무방향 그래프이므로 반대방향도 추가

result=find(N,graph)

print(result)