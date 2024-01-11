#while loop
#while condition:
#       statements
#       increment
def skip3():
    i= 0
    while i< 5:
        i += 1
        if i==3:
            continue
        print(i)


    
def breakloop3():
    i= 5
    while i>=1:
        print(i)
        i=i-1
        if i==3:
            break
skip3()
breakloop3()
    

