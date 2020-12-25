import time

# Вариант 1
time_second = int(input("Введите время в секундах >>> "))
time_format = time.strftime("%H:%M:%S", time.gmtime(time_second))

print(time_format)


# Вариант 2

time_sec = time_second % 60
time_min = (time_second - time_sec) % 3600 // 60
time_hour = time_second // 3600

print(f'{time_hour}:{time_min}:{time_sec}')
