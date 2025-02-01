N = int(input())  # 배열 크기
arr = list(map(int, input().split()))  # 입력 배열
k = int(input())  # 묶음 크기

def sort(k):
  group = [arr[i:i+ N // k ] for i in range(0,N,N // k)]
  for j in range(len(group)):
    group[j].sort()
  print(" ".join(map(str, [num for sublist in group for num in sublist])))
  
sort(k)