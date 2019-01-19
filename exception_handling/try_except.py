"""
Example of try-except error handling
"""

miles_driven = 30
gallons_of_gas_used = 0

try:
    mpg = miles_driven / gallons_of_gas_used
    print(f'Your MPG is {mpg}')
except ZeroDivisionError:
    print('Do you drive an electric car?')


