def check_order(l):
    l2 = []
    l3 = []
    
    for i in l :
        l2.append(i)
    for i in l :
        l3.append(i)
    
    l2.sort()
    l3.sort(reverse=True)
    if len(l) == 0:
        return "The list is empty."
    if l == l2 and l != l3:
        return "The list is in non-decreasing order."
    elif l == l3 and l != l2:
        return "The list is in non-increasing order."
    elif l == l2 and l == l3:
        return "The list is in non-increasing and non-decreasing order."
    else:
        return "The list is in random order."

l = []
while True:
    n = int(input("Enter a number (-1 to end): "))
    if n == -1:
        break
    elif n < 0 or n > 100:
        print("Number is out of range.")
        continue
    l.append(n)
    
print("-----")
print("Original list:")
print(l)
print(f"{check_order(l)}")