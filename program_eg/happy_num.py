def happy_num(num):
    res=0
    for i in range(len(str(num))):
        x=str(num)[i]
        res+=int(x)**2
    while res!=1 or res!=4:
        print(res)
        happy_num(res)
    if res==1:
        print("Give num is happy number")
    elif res==4:
        print("given num is not happy number")

happy_num(37) 