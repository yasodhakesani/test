def prime(num):
    count=0
    if num==1:
        print("its not a prime number")
    
    elif num>1:
        for i in range(1,num+1):
            if num%i==0:
                count+=1
                
            else:
                continue
    if count>2:
        print("its not prime")
    else:
        print("its a prime")

prime(2457)