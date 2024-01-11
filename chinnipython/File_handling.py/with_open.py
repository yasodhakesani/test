with open("sanvi.txt","w") as f:
    f.write("""with open(file_path, mode, encoding) as file:
            generators and decorators:
yield can return one value at a tiime and remember the state of execution
we can write multiple yields but return we can wrtie only once
python version
next()
functions are first class object in python
function also a object in python
outer function inner function
decorator""")
    f.close()

with open("sanvi.txt","r") as f:
    res=f.read()
    print(res)
    print("====================")
with open("chinni.txt","a") as g_file:
    with open("sanvi.txt","r") as f:
        lines=f.readlines()
        g_file.writelines(lines)

with open("chinni.txt","r") as f:
    res=f.read()
    print(res)



