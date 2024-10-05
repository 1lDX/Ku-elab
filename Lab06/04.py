frame = 0
score = 0
while frame < 10:
    pins = 10
    frame += 1
    r = 0
    test = 0
    while r < 2:
        if test == 0:
            print(f"Frame # {frame}")
            down = int(input(f"  Number of pins down: "))
            left = pins - down
            score += down
            test += 1
            if down == 10:  
                break
        else:
            print(f"Frame # {frame}")
            down = int(input(f"  Number of pins down (0-{left}): "))
            score += down
            test += 1
            break
        r += 1
print(f"Total score is {score}")