"""Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]"""

"""l=[23, 65, 19, 90]
for x in range(len(l)):
    pos1=0
    pos2=2
    if x==pos1:
        temp=l[x]
        l[x]=l[pos2]
        l[pos2]=temp
print(l)"""
    
def swap(list,a,b):
    list[a-1],list[b-1]=list[b-1],list[a-1]
    print(list)

l1=[1, 2, 3, 4, 5]
swap(l1,2,5)
swap(l1,1,len(l1))

