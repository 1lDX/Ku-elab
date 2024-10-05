n = int(input())
i = 0
char = str(input())

while True:
    if i <= n:
        i = i+1
        print(char*i)

    if i == n :
        break