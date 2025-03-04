T = int(input())
arr = list(int(input()) for _ in range(T))
def find():
  result = []
  for i in arr:
    dp = [0]*max(4,i+1)
    if i == 0:
      result.append(1)
      continue
    if i<0:
      result.append(0)
      continue
    else:
      dp[0] = 1
      dp[1] = 1
      dp[2] = 2
      dp[3] = 4
      for j in range(4,i+1):
        dp[j] = dp[j-1]+dp[j-2]+dp[j-3]
      result.append(dp[i]) 
  return result

res = find()
for k in res:
  print(k)