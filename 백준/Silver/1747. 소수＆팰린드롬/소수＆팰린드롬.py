def find():
  N = int(input())
  
  def is_prime(n):
    if n == 1:
      return False
    else:
      for i in range(2,int(n**0.5)+1):
        if n % i ==0:
          return False
    return True

  def pal(n):
    s = str(n)
    if s == s[::-1]:
      return True
    else:
      return False

  for k in range(N,10**7):
    if k>98689:
      return 1003001
      break
    else:
      if is_prime(k) and pal(k):
        return k
        break

print(find()) 