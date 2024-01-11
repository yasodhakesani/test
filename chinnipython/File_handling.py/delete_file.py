import os

if os.path.exists("chinni.txt"):
    os.remove("chinni.txt")
else:
    print("file does not exist")

os.rmdir("myfolder")