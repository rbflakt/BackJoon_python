class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, index, delta):
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index  # 가장 낮은 비트 찾기
    
    def sum(self, index):
        s = 0
        while index > 0:
            s += self.tree[index]
            index -= index & -index  # 가장 낮은 비트 제거
        return s
    
    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l - 1)

N,M = map(int,input().split())
arr = list(map(int,input().split()))
fenwick = FenwickTree(len(arr))

for i, val in enumerate(arr, 1):
    fenwick.update(i, val)

test = [list(map(int, input().split())) for _ in range(M)]
for i in range(M):
  print(fenwick.range_sum(test[i][0],test[i][1]))