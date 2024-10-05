import math
new = []
recent = -math.inf
while True:
    n = int(input())
    if n > recent:
        new.append(n)
        recent = n
    elif n == -1:
        break
print(new)