
import requests 

   
# Making a GET request 
r = requests.get('https://www.w3schools.com/python/module_requests.asp') 
  

print(r.url) 
print(r.elapsed)
print(r.status_code)

if r.status_code==200:
    print("success")
elif r.status_code==404:
    print("Not found")


  
