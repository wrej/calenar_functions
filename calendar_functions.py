def is_leap(year):
    if year%4 != 0:
        return False
    elif year%100 != 0:
        return True
    elif year%400 != 0:
        return False
    else: return True

def days_in_month(year, month):
    if month > 12 or month < 1:
        return ValueError('Incorrect month!')
    if year < 1582:
        return ValueError('Not in gregorian calendar!')
    leap = is_leap(year)
    if leap and month == 2:
        return 29
    elif not leap and month == 2:
        return 28
    elif month in [1,3,5,7,8,10,12]:
        return 31
    else: return 30

def day_in_year(year, month, day):
    ndays = 0
    i = 1
    if month > 12 or month < 1:
        return ValueError('Incorrect month!')
    if year < 1582:
        return ValueError('Not in gregorian calendar!')
    if day < 0 or day > 31:
        return ValueError('Incorrect day!')
    if (month == 2 and is_leap(year) == True and day > 29) \
    or (month == 2 and is_leap(year)== False and day > 28):
        return ValueError('Incorrect day!')
    if month not in [1,3,5,7,8,10,12] and day > 30:
        return ValueError('Incorrect day!')
    while i < month:
        ndays += days_in_month(year,i)
        i += 1
    ndays += day
    return ndays
