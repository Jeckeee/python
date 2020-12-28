"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def info(first_name, surname, year, city, email, phone):
    return f'name: {first_name} {surname} \n' \
           f'phone: {phone} \n' \
           f'year: {year} \n' \
           f'email: {email} \n' \
           f'city: {city}'


print(info(
    first_name='John',
    surname='Smith',
    phone='12595666332',
    city='NewYork',
    email='johnsmith@at.com',
    year=1986)
    )

