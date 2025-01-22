def find():
    B, C, D = map(int, input().split())
    burger = sorted(map(int, input().split()), reverse=True)
    side = sorted(map(int, input().split()), reverse=True)
    drink = sorted(map(int, input().split()), reverse=True)

    total_cost = 0
    notdiscount = 0
    sol = []

    min_count = min(B, C, D)

    for i in range(min_count):
        current_set = [burger[i], side[i], drink[i]]
        total_cost += sum(current_set) * 0.9 

    total_cost += sum(burger[min_count:]) 
    total_cost += sum(side[min_count:]) 
    total_cost += sum(drink[min_count:])
    notdiscount += sum(burger[:]+side[:]+drink[:])
    sol.append(int(notdiscount))
    sol.append(int(total_cost))

    return sol

sol = find()
for j in sol:
  print(j)