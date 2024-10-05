incase = str(input())
inpass  = str(input())
length = len(incase)
count = 0
for ch in incase :
    if ch in inpass :
        count+=1
if len(incase) == 2:
    print(0)
    print(f"{0:.2f}")
else :
    percentage = (count/(length-2))*100
    print(count)
    print(f"{percentage:.2f}")