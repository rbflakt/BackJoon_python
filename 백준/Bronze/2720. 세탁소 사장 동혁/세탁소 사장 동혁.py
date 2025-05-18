T = int(input())
for _ in range(T):
  a = int(input())
  if a>=25:
    print(a//25)
    a = a%25
  else:
    print(0)
  if a>=10:
      print(a//10)
      a = a%10
  else:
    print(0)
  if a>=5:
      print(a//5)
      a = a%5
  else:
    print(0)
  if a>=1:
      print(a//1)
  else:
    print(0)