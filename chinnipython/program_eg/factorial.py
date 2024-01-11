def fact(num):
    fact=1
    if num==0:
        print("factorial of 0 is 1")
    elif num>1:
        for i in range(1,num+1):
            fact=fact*i
    print(fact)
fact(4)

#recursive

def fact(n):  
    return 1 if (n==1 or n==0) else n * fact(n - 1);  
  
 

print(fact(5))