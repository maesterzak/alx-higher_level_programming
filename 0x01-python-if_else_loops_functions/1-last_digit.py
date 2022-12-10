#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
first_part = f'Last digit of {number} is {last_digit} '
if last_digit > 5:
    second_part = 'and is greater than 5'
elif last_digit == 0:
    second_part = 'and is 0'
elif last_digit < 6 and last_digit !=0:
    second_part = 'and is less than 6 and not 0'      
print(first_part + second_part)
