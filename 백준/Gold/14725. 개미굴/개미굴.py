N = int(input())

# 트리 생성
gool = {}
for _ in range(N):
    k, *data = input().split()
    cur = gool
    for food in data:
        if food not in cur:
            cur[food] = {}
        cur = cur[food]

#print(gool)
#A = sorted(gool.keys())
#print(A)

# 트리 출력 (재귀
def print_tree(tree, depth):
    for key in sorted(tree.keys()):
        print("--" * depth + key)
        print_tree(tree[key], depth + 1)

print_tree(gool, 0)
