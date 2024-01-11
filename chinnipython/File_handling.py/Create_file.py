#key function for working with files in python is open()
#open() need two params one is filename and mode
#Four different methods for opening a file
"""r-open a file for reading if does not exist raise an error. Default mode is reading
w-open a file for writing if does not exist create new file and if file exist override the file
a-open a file for appending if file does not exits create a file
x-create a specified file,return an error if the file exists"""
import csv
f=open("chinni.txt","x")
print("success")


f=open("chinni1.csv","x")
f.close()