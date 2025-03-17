N, K = map(int,input().split())
seq = list(map(int, input().split()))

def two_pointer(seq, K):
  seq.sort()
  left=0 #리스트의 시작점에서 시작
  right=len(seq)-1 #리스트의 끝점에서 시작
  count=0

  while left < right:
    if seq[left] + seq[right] <= K:
      count+=1
      left+=1
      right-=1
    else:
      right-=1
  return count

print(f"{two_pointer(seq, K)}")