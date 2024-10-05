hw = int(input())
success = float(input())
nisit = int(input())
nisit_score = []
i=0
count = 0
while i<nisit:
    n = int(input())
    nisit_score.append(n)
    i+=1
for score in nisit_score:
    score = score/hw *100
    if score < success:
        count = count+1
print(count)
num = 0
z=0
for num in nisit_score:
    num = num/hw *100    
    if num >= success:
        z = z+1
        print(f"{z} {num:.2f}")
    elif num < success:
        z = z+1
        print(f"({z}) {num:.2f}")
        