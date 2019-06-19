def is_leap(year):
    leap = True
    
    if (year %4==0 and year%100!=0 or year%400 ==0):
        return True
    else:
        return False
