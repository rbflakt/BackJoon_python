N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = (left if left != '.' else None, right if right != '.' else None)

def preorder(node, result):
    if node:
        result.append(node)
        preorder(tree[node][0], result)
        preorder(tree[node][1], result)

def inorder(node, result):
    if node:
        inorder(tree[node][0], result)
        result.append(node)
        inorder(tree[node][1], result)

def postorder(node, result):
    if node:
        postorder(tree[node][0], result)
        postorder(tree[node][1], result)
        result.append(node)

root = "A"

pre_result = []
in_result = []
post_result = []

preorder(root, pre_result)
inorder(root, in_result)
postorder(root, post_result)

print("".join(pre_result))
print("".join(in_result))
print("".join(post_result))