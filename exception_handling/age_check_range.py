"""
Exception handling for user input validation. The user should enter an int, representing a
 year between the current year and 120 years ago.
 But if they make a mistake, they should be allowed to try again.
"""

from datetime import datetime

current_year = datetime.today().year
oldest_year = current_year - 120

while True:

    try:
        birth_year = int(input('Enter the year you were born: '))
        if birth_year > current_year or birth_year < oldest_year:
            raise ValueError
        break
    except ValueError:
        print(f'Please enter a number between {oldest_year} and {current_year}')

age = current_year - birth_year

print(f'Thank you, you were born in {birth_year} which makes you about {age}')


