f=open("chinni.txt","w")
f.write("""To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content""")
f.write("Again wiring into the file")
f.close()