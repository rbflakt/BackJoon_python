def find():
    H, W = map(int, input().split())
    h = list(map(int, input().split()))
    total = 0

    for i in range(1, W - 1):  # 양 끝에서는 물이 고일 수 없으므로 1부터 W-2까지 반복
        left_max = max(h[:i])  # 현재 위치의 왼쪽에서 가장 높은 기둥
        right_max = max(h[i + 1:])  # 현재 위치의 오른쪽에서 가장 높은 기둥
        min_height = min(left_max, right_max)  # 두 높이 중 작은 값 선택

        if min_height > h[i]:  # 현재 높이보다 큰 경우에만 물이 고일 수 있음
            total += min_height - h[i]

    return total

print(find())