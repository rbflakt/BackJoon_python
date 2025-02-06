def messi_fibonacci(m):
    base1 = "Messi"
    base2 = "Messi Gimossi"

    dp_length = {1: len(base1), 2: len(base2)}

    for i in range(3, 50):
        dp_length[i] = dp_length[i - 1] + 1 + dp_length[i - 2]

    n = 50
    while n > 2:
        left_length = dp_length[n - 1]

        if m == 6:
          return "Messi Messi Gimossi"
        if m <= left_length:
            n -= 1  # 왼쪽 서브트리로 이동
        elif m == left_length + 1:
            return "Messi Messi Gimossi"  # 공백 반환
        else:
            m -= left_length + 1  # 오른쪽 서브트리로 이동
            n -= 2
    if n == 1:
        return base1[m - 1]
    return base2[m - 1]



M = int(input())
print(messi_fibonacci(M)) 
