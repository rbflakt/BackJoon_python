def find():
    money = int(input())
    stock = list(map(int, input().split()))

    # BNP 방식
    jun_stock = 0
    jun_rem = money
    for price in stock:
        if jun_rem >= price:
            jun_stock += jun_rem // price
            jun_rem %= price

    # TIMING 방식
    sung_stock = 0
    sung_rem = money
    for i in range(2, len(stock)):
        if stock[i-3] > stock[i-2] > stock[i-1]:
            sung_stock += sung_rem // stock[i]
            sung_rem %= stock[i]
        elif stock[i-3] < stock[i-2] < stock[i-1]:
            sung_rem += sung_stock * stock[i]
            sung_stock = 0

    jun_total = jun_stock * stock[-1] + jun_rem
    sung_total = sung_stock * stock[-1] + sung_rem

    if sung_total > jun_total:
        print("TIMING")
    elif sung_total < jun_total:
        print("BNP")
    else:
        print("SAMESAME")

find()