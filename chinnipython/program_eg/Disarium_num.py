def Disarium(num):
    num=str(num)
    res=0
    for i in range(len(num)):
        
        res+=pow(int(num[i]),i+1)
    
    if int(num)==res:
        print("given number is disarium number {}".format(num))
    else:
        print("given number is not disarium number {}".format(num))


#Disarium(175)