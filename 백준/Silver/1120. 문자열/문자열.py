def find():
  A,B = input().split()
  count = float('inf')
  count_1 = 0
  if len(A) == len(B):
    count = 0
    for i in range(len(A)):
      if A[i] != B[i]:
        count += 1
  else:
    for i in range(len(B)-len(A)+1):
      for j in range(len(A)):
        if A[j] != B[j+i]:
          count_1 += 1
      count = min(count_1,count)
      count_1 = 0

  return count

print(find())