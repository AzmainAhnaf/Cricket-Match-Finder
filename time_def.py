# turn gmt+0 to gmt+6
def add_six_hour(hour, minute, meridian):
    if (1 <= int(hour) and 5 >= int(hour)):
        return f'{str(int(hour) + 6)}:{minute} {meridian}'
    elif (int(hour) == 12):
        return f'6:{minute} {meridian}'
    else:
        time_add = int(hour) - 6
        if (meridian.lower() == 'am'):
            return f'{str(time_add)}:{minute} PM'
        elif (meridian.lower() == 'pm'):
            return f'{str(time_add)}:{minute} AM'

# longify short day name
def day_modify(day):
    if day == 'sat':
        return 'Saturday'
    elif day == 'sun':
        return 'Sunday'
    elif day == 'mon':
        return 'Monday'
    elif day == 'tues':
        return 'Tuesday'
    elif day == 'wed':
        return 'Wedensday'
    elif day == 'thu':
        return 'Thursday'
    elif day == 'fri':
        return 'Friday'
    else:
        return day 

# longify short date name
def date_modify(date):
    month = date[-3:]
    if month == 'jan':
        return f'{date.split()[0]} January'
    elif month == 'feb':
        return f'{date.split()[0]} February'
    elif month == 'mar':
        return f'{date.split()[0]} March'
    elif month == 'apr':
        return f'{date.split()[0]} April'
    elif month == 'may':
        return f'{date.split()[0]} May'
    elif month == 'jun':
        return f'{date.split()[0]} June'
    elif month == 'jul':
        return f'{date.split()[0]} July'
    elif month == 'aug':
        return f'{date.split()[0]} August'
    elif month == 'sep':
        return f'{date.split()[0]} September'
    elif month == 'oct':
        return f'{date.split()[0]} October'
    elif month == 'nov':
        return f'{date.split()[0]} November'
    elif month == 'dec':
        return f'{date.split()[0]} December'
    else:
        return date