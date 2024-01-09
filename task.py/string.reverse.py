new_str=input("enter string: ")
reverse_str=""
i=len(new_str)-1
while i>=0:
    reverse_str+=new_str[i]
    i-=1
    
print(reverse_str)