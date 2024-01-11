def greetings(details):
    match details:
        case [day,name]:
            return (f'Good {day},{name}')
        case [day,*name]:
            msg=''
            for i in name:
                msg+=f'Good {day},{i} \n'
            return msg
        
print (greetings(["Morning", "Ravi"]))
print (greetings(["Afternoon","Guest"]))
print (greetings(["Evening", "Kajal", "Praveen", "Lata"]))