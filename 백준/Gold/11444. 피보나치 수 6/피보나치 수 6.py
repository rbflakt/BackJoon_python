def matrix_multiply(A, B, mod):
    """두 행렬 A와 B를 곱하는 함수 (모듈로 연산 포함)"""
    return [
        [
            (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod,
            (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod,
        ],
        [
            (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod,
            (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod,
        ],
    ]

def matrix_exponentiation(matrix, power, mod):
    """행렬을 거듭 제곱하는 함수"""
    # 단위 행렬
    result = [[1, 0], [0, 1]]
    base = matrix
    
    while power > 0:
        if power % 2 == 1:
            result = matrix_multiply(result, base, mod)
        base = matrix_multiply(base, base, mod)
        power //= 2
    
    return result

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    MOD = 1000000007
    base_matrix = [[1, 1], [1, 0]]
    
    # (n-1)번 제곱한 행렬의 [0][0] 위치가 F(n)을 나타냄
    result_matrix = matrix_exponentiation(base_matrix, n - 1, MOD)
    return result_matrix[0][0]

# 입력
n = int(input())
print(fibonacci(n))