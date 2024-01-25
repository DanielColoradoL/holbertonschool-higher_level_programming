#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
abs = number
factor = 1

if abs < 0:
    abs = -abs
    factor = -1

last_d = factor * (abs % 10)

if last_d > 5:
    add = "and is greater than 5"
elif last_d == 0:
    add = "and is 0"
else:
    add = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last_d} {add}")
