num = int(input("Введите любое число >>> "))

# Version 1
n = num
ls = []

while n > 0:
    ls.append(n % 10)
    n //= 10

max_num = max(ls)
print(f'Version 1 - {max_num}')


# Version 2
n2 = num
max_num = 0
while n2 > 0:
    num = n2 % 10
    if num > max_num:
        max_num = num
    n2 //= 10

print(f'Version 2 - {max_num}')
