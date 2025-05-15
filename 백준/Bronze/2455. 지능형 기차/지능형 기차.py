sol = 0
result = 0
for _ in range(4):
    A, B = map(int, input().split())
    sol = sol - A + B
    result = max(result, sol)
        
print(result)