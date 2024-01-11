#break will stop the current loop and run the next statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x=="banana":
        print(x) #["banana"]
        break

#continue will skip the current iteration and run the next iteration
for x in fruits:
    if x=="banana":
        continue
    print(x)  #["apple", "cherry"]
    