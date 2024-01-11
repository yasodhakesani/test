class Father:
    def father_method(self):
        print("Father class Display method calling")
    def common(self):
        print("father class common method calling")
class Mother:
    def mother_method(self):
        print("Father class Display method calling")
    def common(self):
        print("Mother class common method calling")
class Child(Mother,Father):
    pass

c=Child()
c.common()


