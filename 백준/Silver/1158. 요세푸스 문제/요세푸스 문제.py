import sys
N, K = map(int, sys.stdin.readline().split())
 
a = [i for i in range(1,N+1)]
b = []
c = 0
while a:
  c += K-1
  if c >= len(a):
    c %= len(a)
  b.append(str(a.pop(c)))
print('<', ", ".join(b), '>', sep = '')