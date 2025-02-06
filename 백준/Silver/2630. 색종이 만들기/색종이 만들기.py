import sys
sys.setrecursionlimit(10**5)
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

def same(x,y,size):
  first = arr[x][y]
  for i in range(x,x+size):
    for j in range(y,y+size):
      if arr[i][j] != first:
        return False
  return True

count_1 = 0
count_0 = 0

def check(x,y,size):
  global count_0,count_1
  if same(x,y,size):
    if arr[x][y] == 0:
      count_0 += 1
    if arr[x][y] == 1:
      count_1 += 1
    return

  h = size//2
  tl = check(x,y,h)
  tr = check(x,y+h,h)
  bl = check(x+h,y,h)
  br = check(x+h,y+h,h)
  return count_0,count_1

result = check(0,0,N)
print(count_0)
print(count_1)