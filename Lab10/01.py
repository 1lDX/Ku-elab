i = 0
score = []
while i < 20:
    n = int(input("Enter score: "))
    if n < 0 or n > 10 :
        print("Score is out of range.")
        i -= 1
    elif n > 0 or n < 10 :
        score.append(n)
    i += 1
print("Original list:")
print(score)
i = 0
for i in range(11):
    count = 0
    for n in score:
        if i == n:
            count = count+1
    print(f"{i:>2}","*"*count)