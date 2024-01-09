#Arbitrary Arguments
#if you dont know how many arguments passed into function 
#we can pass n number of argument by adding * before parameter in function
#function will recive the tuple of arguments and we can acess it in the form of tuple

def arb_arg(*cars):
    print(cars)

arb_arg("tata","suzuki","ford")

#o/p ('tata', 'suzuki', 'ford') its is tuple





