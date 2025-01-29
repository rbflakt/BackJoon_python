N = int(input())
arr = [list(map(int,input())) for _ in range(N)]

def same_number(x,y,size):
    first = arr[x][y]
    for i in range(x,x+size):
      for j in range(y,y+size):
        if arr[i][j] != first:
          return False
    return True

def check(x,y,size):
    if same_number(x,y,size):
      return arr[x][y]

    h = size // 2
    tl = check(x,y,h)
    tr = check(x,y+h,h)
    bl = check(x+h,y,h)
    br = check(x+h,y+h,h)

    return f"({tl}{tr}{bl}{br})"

result = check(0,0,N)
print(result)