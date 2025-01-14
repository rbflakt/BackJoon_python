def find():
  T = int(input())
  n = list(int(input()) for _ in range(T))

  def is_prime(n):
    for i in range(2,int(n**0.5)+1):
      if n%i == 0:
        return False
    return True

  result = []
  for i in n:
    for k in range(i//2,1,-1):
      a = i-k
      if is_prime(a) and is_prime(k):
        result.append((k,a))
        break

  for j in result:
    print(j[0],j[1])

find()