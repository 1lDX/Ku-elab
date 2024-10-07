table = (str(input()).split("x"))
bomb = int(input())
location = []

for i in range(bomb):
    position = (input().split(","))
    location.append(position)

for y in range(int(table[0])):
    for x in range(int(table[1])):
        if [str(y),str(x)] in location:
            print("*",end="")
        else :
            empty = 0
            #right
            if [str(y),str(x+1)] in location:
                empty +=1
            #left
            if [str(y),str(x-1)] in location:
                empty +=1
            #up
            if [str(y-1),str(x)] in location:
                empty +=1
            #down
            if [str(y+1),str(x)] in location:
                empty +=1
            #upright
            if [str(y-1),str(x+1)] in location:
                empty +=1
            #upleft
            if [str(y-1),str(x-1)] in location:
                empty +=1
            #downright
            if [str(y+1),str(x+1)] in location:
                empty +=1
            #downleft
            if [str(y+1),str(x-1)] in location:
                empty +=1
            print(empty,end="")
    print("")