"""
Example of try-except-finally error handling
"""

miles_driven = 30
gallons_of_gas_used = 10

try:
    mpg = miles_driven / gallons_of_gas_used  # This statement may raise a ZeroDivisionError
    print(f'Your MPG is {mpg}')
except ZeroDivisionError:
    print('Do you drive an electric car?')  # except block only runs if an exception is raised
finally:
    print('Thank you for using the program ')  # finally block always runs, exception or not

