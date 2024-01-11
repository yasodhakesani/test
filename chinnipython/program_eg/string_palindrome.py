def palindrome(x):
    y=x[::-1]
    if x==y:
        print("its a palindrome")
    else:
        print("its not a palindrome")


palindrome("xyysx")