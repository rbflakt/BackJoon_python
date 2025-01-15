import sys

n = int(sys.stdin.readline())
number = {}
number[0] = 0
number[1] = 1

def fibonacci(n):
    if n in number:
        return number[n]
    else:
        m = n // 2
        if n % 2 == 0:
            number[n] = (fibonacci(m) * (fibonacci(m) + 2 * fibonacci(m-1)))% 1000000007
        else:
            number[n] = (fibonacci(m)**2 + fibonacci(m+1)**2)% 1000000007
    return number[n]

fibonacci(n)
print(number[n])
