score = []
check_score = [0,0,0,0,0,0,0,0,0,0,0]
i=0
def find_mode(l):
    for check in score:
        check_score[check]+=1
    z = 0
    while z<11:
        if check_score[z] == max(check_score):
            print(z)
        z+=1
while i<20:
    n = int(input("Enter score: "))
    if n < 0 or n > 10:
        print("Score is out of range.")
    else :
        score.append(n)
        i+=1
print("-----")
print("Original list: ")
print(score)
print("Mode of scores:")
find_mode(score)