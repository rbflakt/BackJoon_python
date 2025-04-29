arr = list(map(int,input().split()))
result = []
if arr[0] != 1:
    result.append(1-arr[0])
else:
    result.append(0)
if arr[1] != 1:
    result.append(1-arr[1])
else:
    result.append(0)
if arr[2] != 2:
    result.append(2-arr[2])
else:
    result.append(0)
if arr[3] != 2:
    result.append(2-arr[3])
else:
    result.append(0)
if arr[4] != 2:
    result.append(2-arr[4])
else:
    result.append(0)
if arr[5] != 8:
    result.append(8-arr[5])
else:
    result.append(0)
print(*result)