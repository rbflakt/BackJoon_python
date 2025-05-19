A = int(input())
B = int(input())
C = int(input())
sorted_s = sorted(str(A*B*C))
for i in range(10):
    print(sorted_s.count(str(i)))