def num(n):
    sum=0
    if n>0:
        while n>0:
            sum+=n
            n-=1
    elif n<0:
        print("enter positive number")
    print("sum of n numbers",sum)

num(100)
    