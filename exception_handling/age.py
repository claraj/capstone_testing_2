"""
Exception handling for user input validation. The user should enter an int, but
if they make a mistake, they should be allowed to try again.
"""
from datetime import datetime

current_year = datetime.today().year

while True:

    try:
        birth_year = int(input('Enter the year you were born: '))
        break
    except ValueError:
        print('Please enter a number.')

age = current_year - birth_year

print(f'Thank you, you were born in {birth_year} which makes you about {age}')


