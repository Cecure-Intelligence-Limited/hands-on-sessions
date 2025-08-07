'''
Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd.
'''

num = input('Give me a number? ')


print(f'The number you gave me was {num}.')


if num % 2 == 0:  # Pelumi # Adetola
    print(f'{num} is an even number.')
else:
    print(f'{num} is an odd number.')
