x="sd"
try:
    print(int(x))
except:
    print("x is not number")
else:
    print("else block executed")

finally:
    print("finally executed")