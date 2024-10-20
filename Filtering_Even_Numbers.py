"""
Filtering Even Numbers:
In this list comprehension exercise
you will practice using list comprehension
to filter out the even numbers from a series of numbers.
"""

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(interger_num) for interger_num in list_of_strings]
result = [ even_num for even_num in numbers if even_num % 2 == 0 ]
print(result)