N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

def same(x,y,size):
  first = arr[x][y]
  for i in range(x,x+size):
    for j in range(y,y+size):
      if arr[i][j] != first:
        return False
  return True

def check(x,y,size):
  count_1=0
  count_0=0
  count_11=0
  if same(x,y,size):
    if arr[x][y]==-1:
      return (1,0,0)
    if arr[x][y]==0:
      return (0,1,0)
    if arr[x][y]==1:
      return (0,0,1)

  h = size // 3
  counts = [check(x+i*h,y+j*h,h) for i in range(3) for j in range(3)]

  count_1 = sum(count[0] for count in counts)
  count_0 = sum(count[1] for count in counts)
  count_11 = sum(count[2] for count in counts)

  return (count_1,count_0,count_11)

result = check(0,0,N)
print(result[0])
print(result[1])
print(result[2])