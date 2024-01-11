#we can write multiple yields but for return we can write only once
def multiple_yield():
    str1="1st String"
    yield str1
    str2="2nd String"
    yield str2
    str3="3rd String"
    yield str3

for i in multiple_yield():
    print(i)