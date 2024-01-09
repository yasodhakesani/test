def prime(x,y):
    l=list()
    for i in range(x,y+1):
        if i==1:
            continue
        elif i>1:
            count=0
            for j in range(1,i+1):
                if i%j==0:
                    count+=1
                else:
                    continue
            if count==2:
                l.append(i)
    print(l)
prime(14,97)