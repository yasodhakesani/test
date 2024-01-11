import calendar

def Display_cal():
    y=int(input("enter year"))
    m=int(input("enter month")) 
    display=calendar.month(y,m)
    display=calendar.calendar(y)
    print(display)

Display_cal()