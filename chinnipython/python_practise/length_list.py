list=[1, 4, 5, 7, 8]
count=0

for x in list:
    count+=1
print(count)
print(len(list))


res=sum(1 for x in list)
print(res)

