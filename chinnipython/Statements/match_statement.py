"""Python supports Match-Case statement,
 which can also be used as a part of decision making. 
 Following is a simple example which makes use of match statement."""

def checkchar(x):
    match x:
        case "a": print("a is aplhabet")
        case "b": print("b is aplhabet")
        case "c"|"d":print("c or d is alphabet")
        case _: print("no access")

checkchar("_")