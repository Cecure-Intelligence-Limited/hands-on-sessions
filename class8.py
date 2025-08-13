'''
Write a function that takes the lengths of the two shorter sides of a right triangle as
its parameters. Return the hypotenuse of the triangle, computed using Pythagorean
theorem, as the function’s result. Include a main program that reads the lengths of
the shorter sides of a right triangle from the user, uses your function to compute the
length of the hypotenuse, and displays the result.'''


def hyp(a: float, b: float) -> float:
    ''' c = the square root of a^2 + b^2'''
    a_squared = a*a
    print(f'The square of {str(a)} is {str(a_squared)}')

    b_squared = b*b
    print(f'The square of {str(b)} is {str(b_squared)}')

    the_sum = a_squared + b_squared
    print(
        f'The sub of the square {str(b_squared)} and {str(a_squared)} is {str(the_sum)}')

    the_root = the_sum**0.5
    print(f'The root of the sum {str(the_sum)} is {str(the_root)}')

    return the_root


x = float(input('Please input the first short lenght: '))

y = float(input('Please input the second short lenght: '))

print(f'The hyp of the two lenght {x} and {y} is below:')
print(hyp(x, y))
