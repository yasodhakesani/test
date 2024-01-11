import csv
with open("Python.csv","r") as f:
    csv_read=csv.reader(f,delimiter=",")
    for i in csv_read:
        print(i)
