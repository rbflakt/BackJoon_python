N = int(input())
for _ in range(N):
    a,b,c = map(int,input().split())
    print(a*(c-1)+b)