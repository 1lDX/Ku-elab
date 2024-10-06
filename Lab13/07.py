money = int(input("Enter amount of money: "))
k = 0
fiveh =0
h = 0
fifty = 0
twenty = 0
coin10 = 0
coin5 = 0
coin2 = 0
coin1 = 0

if money >= 1000:
    k = money // 1000
    money = money - 1000*k
if money >= 500:
    fiveh = money // 500
    money = money - 500*fiveh
if money >= 100:
    h = money // 100
    money = money - 100*h
if money >= 50:
    fifty = money // 50
    money = money - 50*fifty
if money >= 20:
    twenty = money //20
    money = money - 20*twenty

if money >= 10:
    coin10 = money //10
    money = money - 10*coin10
if money >= 5:
    coin5 = money //5
    money = money - 5*coin5
if money >= 2:
    coin2 = money //2
    money = money - 2*coin2
if money >= 1:
    coin1 = money //1
    money = money - 1*coin1
    
if k > 0:
    print(f"1000: {k}")
if fiveh > 0:
    print(f"500: {fiveh}")
if h > 0:
    print(f"100: {h}")
if fifty > 0:
    print(f"50: {fifty}")
if twenty > 0:
    print(f"20: {twenty}")
if coin10 > 0:
    print(f"10: {coin10}")
if coin5 > 0:
    print(f"5: {coin5}")
if coin2 > 0:
    print(f"2: {coin2}")
if coin1 > 0:
    print(f"1: {coin1}")