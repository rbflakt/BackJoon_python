def arrange_line(N, taller_counts):
    # N명의 자리를 나타내는 리스트(=초기화)
    line = [0] * N
    
    for person in range(1, N + 1):
        taller_count = taller_counts[person - 1]
        # 현재 사람을 배치할 위치를 찾음
        position = 0
        while taller_count > 0 or line[position] != 0:
            if line[position] == 0:  # 빈 자리일 경우
                taller_count -= 1
            position += 1
        line[position] = person
    
    return line

N = int(input())
taller_counts = list(map(int, input().split()))

result = arrange_line(N, taller_counts)
print(" ".join(map(str, result)))