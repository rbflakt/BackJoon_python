N=int(input())
map=list(input())

def count_map(map):
  count=0
  n=len(map)
  for i in range(n):
    visited=[False]*n #방문한 인덱스를 추적하는 리스트
    current_index=i #시작위치
    while not visited[current_index]: #현재 위치를 방문 안했을동안 반복
      visited[current_index]=True #방문을 표시함
      if map[current_index]=='E': #E일때 인덱스 증가 
        current_index+=1
      if map[current_index]=='W': #W일때 인덱스 증가
        current_index-=1

    if current_index==i: #시작 위치로 돌아왔다면
      count+=1 #카운트 증가

  return count

print(count_map(map))