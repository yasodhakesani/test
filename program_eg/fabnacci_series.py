def fab(n):
    num1=0
    num2=1
    next_num=num2

    while n>0:
        print(next_num)
        n-=1
        num1=num2
        num2=next_num
        next_num=num1+num2

fab(10)
