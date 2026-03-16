class employee:
    company = "Google"
    def show(self):
        print(f"The name of the employee is {self.name} and they work at {self.company}")


class programmer(employee):
    company = "Microsoft"
    def showlanguage(self):
        print(f"The name of the programmer is {self.name} and he is good with {self.language}") 



a=employee()
b=programmer()
print(a.company,b.company)