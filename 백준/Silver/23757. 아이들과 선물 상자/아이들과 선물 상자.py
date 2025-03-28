import heapq

N, M = map(int, input().split())
present = list(map(int, input().split()))
wish = list(map(int, input().split()))

present = [-p for p in present]
heapq.heapify(present)

for w in wish:
    if not present:
        print("0")
        break

    max_present = -heapq.heappop(present)  

    if max_present < w:
        print("0") 
        break

    remaining = max_present - w
    if remaining > 0:
        heapq.heappush(present, -remaining)
else:
    print("1") 