list= [100, 50, 65, 82, 23]

for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        
        if(list[i]>=list[j]):
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
         
print(list)


for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        
        if(list[i]>=list[j]):
            
            list[i],list[j]=list[j],list[i]
           
         
print(list)

        

