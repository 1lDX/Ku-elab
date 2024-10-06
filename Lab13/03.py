n = int(input())
i = 0
ls = []
paper = []
while i<n:
    b = int(input())
    ls.append(b)
    i+=1

ls.sort(reverse=True)
result = int(input())

for i in ls:
    r = result//i
    result = result-(i*r)
    paper.append(r)

for i in range(len(ls)):
    print(f"{ls[i]}: {paper[i]}")