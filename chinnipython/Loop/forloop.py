"""for condtion in iteration:
	run the statements
    """
for x in  range(6):
	if x==4:
		break
	print(x)
else:
	print("finally")

for x in  range(6):
	if x==4:
		continue
	print(x)
else:
	print("finally")
	
fruits = ["apple", "banana", "cherry"]

#else in for loop:
#else keyword in a for loop specifies a block of code to be executed when the loop is finished:
#below loop else will not execute since iteration not completed
for x  in fruits:
	if x=="banana":
		break
else:
	print("Loop completed iterations")
	
#below loop else will  execute since iteration completed	
for x  in fruits:
	print(x)
else:
	print("Loop completed iterations")
	


#Nested for loop:
for x in range(2):
	for y in range(2):
		print(x,y)	

#break statement : we can stop the current loop and execute the next set of instructopn
def list(a):
	for x in fruits:
		if a==x:
			print(x,"present")
			break
		else:
			print(x,"not equal to input",a)
	
list("apple")
list("hsddk")


    

