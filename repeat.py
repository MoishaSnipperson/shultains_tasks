#!/usr/bin/python3

"""
#9: Повторение строки
Сложность: 2 из 10
Напишите программу repeat.py, которая получает из первого аргумента командной строки слово, 
а из второго число N, а после повторяет полученное слово N раз.
https://shultais.education/lms/courses/python-3/tasks/9
"""

import sys

print(sys.argv[1] * int(sys.argv[2]))