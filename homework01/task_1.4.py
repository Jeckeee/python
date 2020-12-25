n = int(input("Введите любое число >>> "))

ls = []

while n > 0:
    ls.append(n % 10)
    n //= 10

r = max(ls)
print(r)
