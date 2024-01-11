file1 = open("Employees.txt", "w") 
"""lst = [] 
for i in range(3): 
    name = input("Enter the name of the employee: ") 
    lst.append(name) 
      
file1.writelines(lst) 
file1.close() 
print("Data is written into the file.")  """
file1 = open("Employees.txt", "r") 
r=file1.read()
print(r)