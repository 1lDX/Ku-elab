import math
def find_sd(l,avg):
    if len(l) == 1:
        return 0
    up = 0
    for i in l :
        up += (i - avg)**2
    result = up/(len(l)-1)
    return math.sqrt(result)

scores = []

while True:
    score = float(input("Enter score: "))
    if score == -1:
        break
    if score < 0 or score > 100:
        print("Score is out of range.")
        continue   
    scores.append(score)
if len(scores):
    print(f"Maximum score is {max(scores):.2f}.")
    print(f"Minimum score is {min(scores):.2f}.")
    print(f"Average score is {sum(scores)/len(scores):.2f}.")
    print(f"Standard deviation is {find_sd(scores,sum(scores)/len(scores)):.2f}.")