import csv
with open("Python.csv","w") as csvfile:
    headername=['first_name', 'last_name', 'Rank'] 
    writer=csv.DictWriter(csvfile,fieldnames=headername)
     
    writer.writerow({'Rank': 'B', 'first_name': 'Parker','last_name': 'Brian'})    
    writer.writerow({'Rank': 'A', 'first_name': 'Smith','last_name': 'Rodriguez'})    
    writer.writerow({'Rank': 'B', 'first_name': 'Jane','last_name': 'Oscar'})    
    writer.writerow({'Rank': 'B', 'first_name': 'Jane','last_name': 'Loive'})    

    print("writing completed")
