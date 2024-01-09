def calculator(x):
        
    
        
            a=input("enter first number to perform operations")
            b=input("enter second number to perform operations")
            res=0
            if x.upper()=="ADD":
                res=int(a)+int(b)
                print("sum of two numbers",res)
            elif x.upper()=="SUBTRACT":
                res=int(a)-int(b)
                print("subtract two number",res)
            elif x.upper()=="MULTIPLY":
                res=int(a)*int(b)
            elif x.upper()=="DIVIDE":
                try:
                    res=int(a)/int(b)
                except:
                    print("Zero Division Error")
            else:
                print("enter only operations add,subtract,multiply,divide")


calculator("add") 