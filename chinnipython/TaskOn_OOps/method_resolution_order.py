class Father:
    def __init__(self):
        pass
    def common(self):
        print("Father Class Common Method")
class Mother:
    def common(self):
        print("Mother Class Common Method")
class Child(Mother,Father):
    pass

c=Child()
c.common() #Mother class will call common method