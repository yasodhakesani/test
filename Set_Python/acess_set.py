thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

if "apple" in thisset:
    print(True)

(x,*z)=thisset
print(x,z)