def format_(word:str):
    point = word.find("=")
    left = word[0:point].strip()
    right = word[point+1:].strip()
    length = len(left)
    return left+" = "+right, length
maxlength = 0
s1 = []
index = 0
while True : 
    word = str(input())
    if word == "-1":
        break
    result = format_(word)
    if result[1] > maxlength:
        maxlength = result[1]
    s1.append(result)
for i in s1:
    print(f'{" "*(maxlength-i[1])}{i[0]}')