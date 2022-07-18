#!/usr/bin/python3

"""
#1: Основной заголовок
Сложность: 1 из 10
Напишите программу, которая получает из первого аргумента командной строки слово, 
а после печатает это слово большими буквами. Слово должно быть помещено в центр строки длиной 
20 символов и отбито справа и слева пробелами.
https://shultais.education/lms/courses/python-3/tasks/1
"""

import sys

sup_string = sys.argv[1].upper().center(20, '+')

print(sup_string)
print(len(sup_string))