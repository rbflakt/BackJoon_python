def square(k):
  for i in range(N-k+1):
    for j in range(M-k+1):
      if matrix[i][j]==matrix[i+k-1][j]==matrix[i][j+k-1]==matrix[i+k-1][j+k-1]:#모서리가 같은 숫자
         return True
  return False

N,M=map(int,input().split())
matrix=[list(map(int,list(input()))) for _ in range(N)]

size=min(M,N)

for t in range(size,0,-1):
  if square(t):
    print(t**2)#정사각형 크기
    break