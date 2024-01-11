import armstrong
def armstrong_interval(x,y):
    for i in range(x,y+1):
        armstrong.armstrong(i)

armstrong_interval(200,407)