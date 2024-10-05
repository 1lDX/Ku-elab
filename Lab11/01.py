n = int(input())
i = 1
c = 0
while i<=n:
    print("|"+" "*(n-i)+"*"*i+"*"*c+" "*(n-i)+"|")
    i+=1
    c+=1