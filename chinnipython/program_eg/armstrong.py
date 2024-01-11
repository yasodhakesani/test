def armstrong(num):
    res=0
    if num>0:
        L=str(num)
        
        for i in range(len(L)):
            res+=pow(int(L[i]),len(L))
        if num==res:
            print("{} Number is armstrong".format(num))
        else:
            print("{} Number is not a armstrong".format(num))

#armstrong(407)