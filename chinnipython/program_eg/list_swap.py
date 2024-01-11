list=[12, 35, 9, 56, 24]
def swap(list):
    list[0],list[-1]=list[-1],list[0]
        
    return list

print(swap(list))