#! Python 3
# * Time_calculator - Takes in Current time along with Duration and an optional Day and will return the Expected time and day after adding that duration

def add_time(start, duration, day=''):
    new_time = ''
    dayslater = ''  # ? A variable to store the string based on number of days passing
    countdays = 0  # ? A variable to store the number of days passing
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    # ? converting the day to a format which can be used as same as list
    day = day.lower().title()

    time, amorpm = start.split()
    hour, minute = map(int, time.split(':'))
    addhours, addminutes = map(int, duration.split(':'))

    new_hour = hour + addhours
    new_minute = minute + addminutes

    # Checking all condition from here on.

    # Automatically increases the new_hours with 1 with minutes go more than 60, to show the next hour and resetting new_minutes to 0
    if new_minute >= 60:
        new_hour += 1
        new_minute -= 60

    # This condition is just for formatting since minutes always are double digits. This condition just makes sure that if New_minutes is a single digit number then adds a '0' before it.
    if new_minute < 10:
        new_minute = '0'+str(new_minute)

    # This condition checks if its the next day, how many days have passed, and changes 'AM' to 'PM'. Number of days only increases if 'PM' changes to 'AM' showing that a new day starts.
    while new_hour >= 12:
        if new_hour > 11:
            if amorpm == 'PM':
                amorpm = 'AM'
                countdays += 1
            else:
                amorpm = 'PM'
        new_hour -= 12

    # Since time cannot be '00:30', this condition converts '00' to '12'
    if new_hour == 0:
        new_hour = 12

    # This checks how many days have passed and includes the neccessary words to the string 'dayslater'.
    if countdays == 1:
        dayslater = " (next day)"
    elif countdays > 1:
        dayslater = ' ('+str(countdays)+' days later)'
    else:
        dayslater = ''

    # This try-except is to make the find out the day using the No. of days passed in countDays.
    try:
        dayIndex = days.index(day)
        for i in range(countdays):
            dayIndex += 1
            if dayIndex > 6:
                dayIndex = 0
    except:
        dayIndex = None

    new_time = str(new_hour)+':'+str(new_minute)+' ' + \
        str(amorpm)

    if dayIndex != None:
        new_time = new_time + ', ' + days[dayIndex] + dayslater
    else:
        new_time = new_time+dayslater

    return new_time.rstrip()


# print(add_time("11:55 AM", "3:12"))
