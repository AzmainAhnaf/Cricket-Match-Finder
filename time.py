def add_six_hour(hour, minute, meridian):
    if (1 <= int(hour) and 5 >= int(hour)) or int(hour) == 12:
        return f'{str(int(hour) + 6)}:{minute} {meridian}'
    else:
        time_add = int(hour) - 6
        if (meridian.lower() == 'am'):
            return f'{str(12 + time_add)}:{minute} PM'
        elif (meridian.lower() == 'pm'):
            return f'{str(12 + time_add)}:{minute} AM'

print(add_six_hour('6', '00', 'pm'))

