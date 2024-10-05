f = int(input("Enter the first number: "))
s = int(input("Enter the second number: "))

f_gcd = f
s_gcd = s
gcd = 0
while True:
    if s_gcd > f_gcd:
        s_gcd,f_gcd=f_gcd,s_gcd

    f_gcd = f_gcd % s_gcd
    if f_gcd == 0:
        gcd = s_gcd
        break


print(f"  >> gcd({f}, {s}) ={gcd:>7}")
print(f"  >> lcm({f}, {s}) ={(f*s)//gcd:>7}")