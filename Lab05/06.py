n = int(input())
count = 0
i = 0
while True:
    i += n%10
    n = n//10
    if n == 0:
        break
if i % 9 == 0:
    print(f'Yes {i}')
elif i % 9 >=1:
    print(f'No {i%9}')