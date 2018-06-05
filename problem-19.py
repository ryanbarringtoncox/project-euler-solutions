#!/usr/bin/python

end_year = 2001
current_day = 1
current_month = 1
current_year = 1901
current_day_of_week = 't'
sundays_on_first_of_month_count = 0

next_day_of_week = {
    'm' : 't',
    't' : 'w',
    'w' : 'r',
    'r' : 'f',
    'f' : 's',
    's' : 'u',
    'u' : 'm'
}

def get_leap_year_status(year):
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    if year % 400 == 0:
        return True
    return False

def flip_month(year, month, day):
    is_leap_year = get_leap_year_status(year)
    if (month == 2 and day == 29 and is_leap_year) or (month == 2 and day == 28 and not is_leap_year) or \
        (month in [9,4,6,11] and day == 30) or (month in [1,3,5,7,8,10] and day == 31):
        return True
    else:
        return False

if __name__ == "__main__":

    while current_year < end_year:

        # print "%s %d/%d/%d" % (current_day_of_week, current_month, current_day, current_year)

        # count sundays on the first of the month
        if current_day == 1 and current_day_of_week == 'u':
            sundays_on_first_of_month_count += 1

        # flip year
        if current_month == 12 and current_day == 31:
            current_month = 1
            current_day = 1
            current_year += 1

        # flip month
        elif flip_month(current_year, current_month, current_day):
            current_day = 1
            current_month += 1

        # flip day
        else:
            current_day += 1

        # always increment day of week
        current_day_of_week = next_day_of_week[current_day_of_week]

    print sundays_on_first_of_month_count
