x=int(input("Enter the size of list: "))
new_list=[]
for i in range(x):
    L=input()
    new_list.append(L)
print(new_list)

new_dict=dict()
for i in range(len(new_list)):
    x=new_list.count(new_list[i])
    new_dict[new_list[i]]=x

print(new_dict)