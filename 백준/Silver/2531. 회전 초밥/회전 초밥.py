N,d,k,c = map(int,input().split())
sushi = [int(input()) for _ in range(N)]

def find(N,k,c):
  left, right = 0, k-1
  max_sushi=0

  while left<N:
    current_range = [sushi[(left+i) % N] for i in range(k)]
    sushi2=set(current_range)

    if c not in sushi2:
      sushi2.add(c)
      
    max_sushi=max(max_sushi, len(sushi2))

    left+=1
    right+=1

  return max_sushi

print(f"{find(N,k,c)}")