'''
It is commonly said that one human year is equivalent to 7 dog years. 
However this simple conversion fails to recognize that dogs reach adulthood in approximately two years.
As a result, some people believe that it is better to count each of the first two human years as 10.5 dog years,
and then count each additional human year as 4 dog years.
Write a program that implements the conversion from human years to dog years  described in the previous paragraph. 
Ensure that your program works correctly for conversions of less than two human years and for conversions of two or more human years.
Your program should display an appropriate error message if the user enters  a negative number.


1 year  = 5.25
2 years  = 10.5
3 years  = 14.5
4 years  = 18.5

'''

user_input = input('Give me an age: ')


# try:
#     user_input = int(human_years)
# except Exception:
#     print('Age must be a number')


# if human_years < 0:
#     print('Age can not be negetive.')
# elif human_years <= 2:
#     dog_year = human_years*10.5
#     print(dog_year)
# else:
#     first_two = 2*10.5
#     remaining = human_years - 2 * 4
#     dog_year = first_two + remaining
#     print(dog_year)

if not user_input.isdigit():
    print("Invalid input: Please enter a number.")
else:
    human_years = int(user_input)
    if human_years <= 2:
        # a = 5.25
        # b = (human_years - 2) * 4
        dog_age = 5.25

        print("Your dog age is:", dog_age)
    else:
        a = 10.5
        b = (human_years - 2) * 4
        dog_age = a + b

        print("Your dog age is:", dog_age)
