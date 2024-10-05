word = str(input())
x = word.split(",")
result = ""
for i in x:
    result += '"'+i.strip()+'",'
print (result[0:-1])