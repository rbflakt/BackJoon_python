import math

def find():
  number = []
  while True:
    n = int(input())
    if n == 0:
      break
    number.append(n)

  result = []
  for i in number:
    k = math.factorial(2*i)/(math.factorial(i+1)*math.factorial(i))
    result.append(int(k))

  for j in result:
    print(j)

find()