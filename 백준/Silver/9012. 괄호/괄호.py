def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        else:
            if not stack:
                return 'NO'
            stack.pop()
    return 'YES' if not stack else 'NO'

T = int(input())
for _ in range(T):
    s = input()
    print(solution(s))