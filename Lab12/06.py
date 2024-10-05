def normal(n):
    print(int(n)+1)

def float_func(n:str):
    if n[-3] in ("."):
        print(float(n)+1)
    else:
        return print("ERROR")

def comma(n:str):
    for ch in n[-4::-4]:
        if ch == ",":
            n = n.replace(",","")
            result = int(n)+1
        else:
            result = "ERROR"
    print(result)  

def dotcomma(n:str):
    if n[-3] in ("."):
        for ch in n[-7::-4]:
            if ch == ",":
                n = n.replace(",","")
                result = float(n)+1
            else:
                result = "ERROR"
        print(result)    
    else:
        return print("ERROR")
    
def alphabet(n):
    for i in n:
        if i in ",." :
            continue        
        if (ord(i)) < 48 or (ord(i) > 57):
            return False

    return True

n = str(input())
if alphabet(n) :
    if ("." not in n) and ("," not in n):
        normal(n)
    elif ("." in n) and ("," not in n):
        float_func(n)
    elif ("," in n) and ("." not in n):
        comma(n)
    elif ("." in n) and ("," in n):
        dotcomma(n)
else:
    print("ERROR")