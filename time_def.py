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

# longify short date name
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