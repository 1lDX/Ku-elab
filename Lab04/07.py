level = int(input("Enter level pokemon: "))
ball = str(input("Enter level pokeball: "))
dis = int(input("Enter distance: "))
per = 0

if level >= 0 and level <= 100 and (ball == "h" or ball == "H"):
    per = 0.01
elif  level >=0 and level <= 40 and(ball == "m" or ball == "M"):
    per = 0.03
elif  level >=41 and level <= 60 and (ball == "m" or ball == "M"):
    per = 0.05
elif  level >=61 and level <= 100 and (ball == "m" or ball == "M"):
    per = 0.08
elif  level >=0 and level <= 40 and (ball == "l" or ball == "L"):
    per = 0.05
elif  level >=41 and level <= 60 and (ball == "l" or ball == "L"):
    per = 0.03
elif  level >=61 and level <= 100 and (ball == "l" or ball == "L"):
    per = 0.1

s = 100 - (level * dis * per)

if s < 0 :
    s = 0
elif s > 100:
    s = 100

print(f"{s:.2f} percent.")