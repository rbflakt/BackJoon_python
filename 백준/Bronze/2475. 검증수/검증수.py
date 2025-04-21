a=0
arr = list(map(int,input().split()))
for i in range(5):
    a += arr[i]**2
print(a%10)