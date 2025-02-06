K = int(input())
arr = list(map(int,input().split()))

class Node:
  def __init__(self,key):
    self.left = None
    self.right = None
    self.value = key

def inorder(arr,start,end,level,level_info):
  if start>end:
    return None
  mid = (start+end)//2
  node = Node(arr[mid])

  if level not in level_info:
    level_info[level] = []
  level_info[level].append(node.value)

  node.left = inorder(arr,start,mid-1,level+1,level_info)
  node.right = inorder(arr,mid+1,end,level+1,level_info)

  return node

level_info = {}
root = inorder(arr,0,len(arr)-1,1,level_info)
for i in sorted(level_info):
  print(*level_info[i])