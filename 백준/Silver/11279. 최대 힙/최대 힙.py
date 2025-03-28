import heapq
import sys
input = sys.stdin.readline

arr = []
N = int(input())

for _ in range(N):
  a = int(input())
  if a == 0:
    if arr:
      print(-heapq.heappop(arr))
    else:
      print("0")
  else:
      heapq.heappush(arr,-a)