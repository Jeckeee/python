import time

# Вариант 1
time_second = 3849  # int(input("Введите время в секундах >>> "))
time_format = time.strftime("%H:%M:%S", time.gmtime(time_second))

print(time_format)

# Вариант 2

time_hour = time_second // 3600
time_min = time_second % 3600 // 60
time_sec = time_second % 60

if time_hour < 10:
    time_result = f'0{time_hour}:'
else:
    time_result = f'{time_hour}:'

if time_min < 10:
    time_result += f'0{time_min}:'
else:
    time_result += f'{time_min}:'

if time_sec < 10:
    time_result += f'0{time_sec}'
else:
    time_result += f'{time_sec}'

print(time_result)
