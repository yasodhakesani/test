t = ("apple", "banana", "cherry")
print(t[0])
print(t[0:])
print(t[0:3:2])
print(t[-3:])

for x in t:
    print(x)
    if "apple" in x:
        print(True)

i=0;
while i<len(t):
    print(t[i])
    if "apple" in t[i]:
        print(True)
    i+=1;