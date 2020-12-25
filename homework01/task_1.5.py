profit = int(input("Введите выручку >>> "))
costs = int(input("Введите издержки >>> "))

if profit > costs:
    print(f"Прибыль составила {profit - costs:.2f}")
    workers = int(input("Введите количество сотрудников >>> "))
    print(f"Прибыль на одного сторудника сотавила {profit / workers:.2f}")

elif profit == costs:
    print("Прибыль равна нулю!")

else:
    print("Фирма работает в убыток!")
