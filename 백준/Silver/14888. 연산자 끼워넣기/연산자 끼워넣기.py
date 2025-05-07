from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))
op_input = list(map(int, input().split()))

ops = [op for count, op in zip(op_input, ['+', '-', '*', '/']) for _ in range(count)]
all_combinations = set(permutations(ops))

def find(nums, op):
    nums = nums[:]
    ops = list(op)
    result = nums.pop(0)

    while ops:
        operator = ops.pop(0)
        num = nums.pop(0)

        if operator == '+':
            result += num
        elif operator == '-':
            result -= num
        elif operator == '*':
            result *= num
        elif operator == '/':
            if result < 0:
                result = -(-result // num)
            else:
                result //= num

    return result


results = [find(arr, comb) for comb in all_combinations]

print(max(results))
print(min(results))