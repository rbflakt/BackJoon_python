N = int(input())
arr = list(int(input()) for _ in range(N))

def find():
  dp = [0] * (N)
  if N == 1:
    return arr[0]
  if N == 2:
    return arr[0]+arr[1]
  for i in range(N):
    if i == 0:
      dp[0] = arr[0]
    if i == 1:
      dp[1] = arr[0] + arr[1]
    if i == 2:
      dp[2] = max(dp[0]+arr[2],arr[1]+arr[2])
    if i>=3:
      dp[i] = max(dp[i-2]+arr[i],arr[i]+arr[i-1]+dp[i-3])
  return dp[N-1]

print(find())