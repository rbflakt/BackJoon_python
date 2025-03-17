def find():
  N = int(input())
  arr = []
  for i in range(N):
    xi,yi = map(int,input().split())
    arr.append((xi,'start'))
    arr.append((yi,'end'))

  arr.sort(key = lambda x: (x[0],x[1] == 'end')) #튜플으로 저장

  max_overlap = 0
  current_overlap = 0

  #for x,a in arr:
    #if current_overlap > 0 and last is not None:

  i = 0
  while i < len(arr):
    x,a = arr[i]
    same = 0
    while i < len(arr) and arr[i][0] == x:
      if arr[i][1] == 'start':
        current_overlap += 1
      if arr[i][1] == 'end':
        current_overlap -= 1
      same += 1
      i += 1

    max_overlap = max(max_overlap,current_overlap)

    if same > 1:
      continue

  return max_overlap

print(find())