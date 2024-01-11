def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print("Its a leap year")
            else:
                print("Its not a leap year")
        else:
            print("its a leap year")
    else:
        print("Its not a leap year")

leap_year(1900)