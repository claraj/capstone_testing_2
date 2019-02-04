""" Program to save the number of hours worked for every day in the week
Alerts user with printed and audible alert if total hours for week is less than min_hours.  """


def main():
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    min_hours = 30

    hours_worked = get_hours(days)
    display_hours(hours_worked)
    total = total_hours(hours_worked)
    display_total(total)
    alert_not_meet_min_hours(total, min_hours)


def get_hours(days):
    hours_worked = {}
    for day in days:
        hours = get_hours_for_day(day)
        hours_worked[day] = hours
    return hours_worked


def get_hours_for_day(day):
    while True:
        try:
            return float(input(f'Enter hours worked for {day}: '))
        except:
            print('Enter a number')
        

def display_hours(hours_worked):
    print(f'{"Day":<15}{"Hours Worked":<15}')
    for day, hours in hours_worked.items():
        print(f'{day:<15}{hours:<15}')


def total_hours(hours_worked):
    return sum(hours_worked.values())


def display_total(total):
    print(f'Total hours worked: {total}')
    

def alert_not_meet_min_hours(hours, min):
    if hours < min:
        alert()
        print('You worked less than the minimum number of hours')


def alert():
    """ If this doesn't make a sound on Mac, go into your terminal 
    settings, advanced tab, check Audible bell """
    print('\a')
    

if __name__ == '__main__':
    main()

