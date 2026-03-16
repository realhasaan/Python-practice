class employee:
    company = "Google"
    name="John"
    def show(self):
        print(f"The name of the employee is {self.name} and they work at {self.company}")

class coder:
    language = "Python"
    def languageset(self):
        print(f"The languae by default is {self.language}")
    

class programmer(employee, coder):
    company = "Microsoft"
    def showlanguage(self):
        print(f"The name of the programmer is {self.name} and he is good with {self.language}") 



a=employee()
b=programmer()
a.show()
b.show()
b.languageset()
b.showlanguage()
