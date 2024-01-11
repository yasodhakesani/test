
list = ["banana","apple", "cherry"]
#break in for loop list
for x in list:
    print(x)
    if "apple" in x:
        print("apple present in list")
        break
#continue in for loop list
for x in list:
    if "apple" in x:
        continue
    print(x)

#for loop list using range
list1=[]
for x in range(len(list)):
    list1.append(list[x])
print(list1)


#while loop list
list2=[]
i=0
while i<len(list):
    list2.append(list[i])
    i+=1
print(list2)

        