N = int(input())
A = sorted(map(int,input().split()))
B = sorted(map(int,input().split()), reverse = True)

result = 0
for i in range(N):
  result += A[i]*B[i]

print(result)