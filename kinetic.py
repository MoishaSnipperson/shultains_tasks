#!/usr/bin/python3

"""
#2: Кинетическая энергия
Сложность: 2 из 10
Напишите программу, которая получает из первого аргумента командной строки массу тела,
а из второго его скорость, а после печатает кинетическую энергию этого тела.
Масса и скорость могут быть как целыми числами, так и вещественными.
https://shultais.education/lms/courses/python-3/tasks/2
"""

import sys

# Получаем аргументы командной строки и сразу
# преобразовываем их к вещественным числам.
m = float(sys.argv[1])
v = float(sys.argv[2])
print(((v **2 ) * m) / 2)