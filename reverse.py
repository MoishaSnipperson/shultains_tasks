#!/usr/bin/python3

"""
#7: В обратном порядке
Сложность: 2 из 10
Напишите программу, которая получает из первого аргумента командной строки слово, а после печатает его задом наперед.
https://shultais.education/lms/courses/python-3/tasks/7
"""

import sys

print(sys.argv[1][::-1])
print("".join(reversed(sys.argv[1])))