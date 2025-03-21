from collections import defaultdict

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
result = defaultdict(int)
#values = {chr(N): int(input()) for i in range(N)}

first_1 = max(arr[i][0] for i in range(N))
first_2 = max(arr[i][1] for i in range(N))
#last_1 = min(arr[i][0] for i in range(N))
#last_2 = min(arr[i][1] for i in range(N))


for i in range(N):
    if arr[i][0] == first_1 and arr[i][1] == first_2:
      result[i] = 1
    #elif arr[i][0] == last_1 and arr[i][1] == last_2:
      #result[i] = N
    else:
      count = 1
      for j in range(N):
          if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            count += 1
      result[i] = count

print(" ".join(str(result[key]) for key in result))