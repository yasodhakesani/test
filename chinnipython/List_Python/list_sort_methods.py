list = ["orange", "mango", "kiwi", "pineapple", "banana"]
#sorting is not posible if list contain alpha,number
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
list.sort()
print(list)



#reverse=true will do descending order
list.sort(reverse=True)
print(list)

#customize sort function
#we can customize of your own function by using key=function

def fun(n):
    return abs(n-23)

list=[100, 50, 65, 82, 23]
list.sort(key=fun)
print(list)

#Case Insensitive Sort 
#if list have capital letter sort will pick random not based on alphabetic order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#if you want to get sort order for the above list perform lower function
thislist.sort(key=str.lower)
print(thislist)

#if you want reverse order list without sorting in alphabet order
list = ["orange", "mango", "kiwi", "pineapple", "banana"]
list.reverse()
print(list)

l= [1, 2, 3, 4, 6, 7, 8]
print(sorted(l,reverse=True))

list=[100, 50, 65, 82, 23]
print(sorted(list))

L = [15, 3, 11, 7]
def fun(x):
    return x%7

print(sorted(L,key=fun))
