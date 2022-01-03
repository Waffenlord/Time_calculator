def add_time(start, duration, day = None):
    l_initial = start.split()
    l_numbers = l_initial[0].split(':')
    l_duration = duration.split(':')
    days_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    days_later = 0
    time_day = l_initial[1]
    init_hour = int(l_numbers[0])
    add_hour = int(l_duration[0])
    minutes = 0

    if int(l_numbers[1]) + int(l_duration[1]) < 60:
        minutes = int(l_numbers[1]) + int(l_duration[1])
    elif int(l_numbers[1]) + int(l_duration[1]) >= 60: 
        minutes = (int(l_numbers[1]) + int(l_duration[1])) - 60
        add_hour += 1 
    
    if len(str(minutes)) == 1:
        minutes = '0' + str(minutes)

    
    while add_hour > 0:
        if init_hour == 12:
            init_hour = 0
            
        init_hour += 1
        add_hour -= 1
    
        if init_hour == 12 and time_day == 'AM':
            init_hour = 0
            time_day = 'PM'
            continue
        elif init_hour == 12 and time_day == 'PM':
            init_hour = 0
            time_day = 'AM'
            days_later += 1
            continue

    if init_hour == 0:
        init_hour = 12
        
    if day == None:
        if days_later < 1:
            return f'{init_hour}:{minutes} {time_day}'
        elif days_later == 1:
            return f'{init_hour}:{minutes} {time_day} (next day)'
        else:
            return f'{init_hour}:{minutes} {time_day} ({days_later} days later)'
    else:
        if days_later < 1:
            return f'{init_hour}:{minutes} {time_day}, {day.lower().title()}'
        elif days_later == 1:
            idx = days_week.index(day.lower())
            idx += 1
            if idx > len(days_week) - 1:
                idx -= len(days_week)
            return f'{init_hour}:{minutes} {time_day}, {days_week[idx].title()} (next day)'
        else:
            idx = days_week.index(day.lower())
            counter = days_later
            while counter > 0:
                idx += 1
                counter -=1
                if idx > len(days_week) - 1:
                    idx -= len(days_week)
                    continue
            return f'{init_hour}:{minutes} {time_day}, {days_week[idx].title()} ({days_later} days later)'
            




