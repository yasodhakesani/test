txt="hello"
def even(txt):
    print(txt[0:len(txt):2])
def odd(txt):
    print(txt[1:len(txt):2])

even("hello")
odd("hello")

print(txt[0:])
print(txt[-5:])
for x in txt:
    print(x)

for x in range(len(txt)):
    print(txt[x])
        


