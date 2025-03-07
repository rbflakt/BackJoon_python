N = int(input())
def find():
  dp = [0]*max(3,N)
  for i in range(N):
      dp[0] = 1
      dp[1] = 2
      dp[2] = 3
      for j in range(3,i+1):
        dp[j] = dp[j-1]+dp[j-2]
  return dp[N-1]%10007

print(find())