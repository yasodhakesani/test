list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#Direct changing the list by refering the index 
#it will change original list
list[2]="carrot"
print(list)
print(len(list))
list[1:3]=["melon","dragon"]
print(list)
#len of the list is 7(0-6 index) but if you try to insert 7th index including existing index also it will add
#['apple', 'melon', 'dragon', 'orange', 'kiwi', 'melon', 'papaya', 'pulpi']
list[6:7]=["papaya","pulpi"]
print(list)
#5:7 instead of two elements we are adding 5th element only 
#it will consider as 6th element as empty and remove the existing 6th element
#['apple', 'melon', 'dragon', 'orange', 'kiwi', 'melon', 'papaya', 'pulpi']
#['apple', 'melon', 'dragon', 'orange', 'kiwi', '5thelement', 'pulpi']
list[5:7]=["5thelement"]
print(list)

