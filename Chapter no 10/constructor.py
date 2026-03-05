class empl:
    lang="English"   #class attribute 
    slary=50000
   
    def getinfo(self):
        print(f"Language: {self.lang}, Salary: {self.salary}")
    #dunder method
    def __init__(self,name,salary,lang):
        self.name=name
        self.salary=salary
        self.lang=lang

        print("I am creating an object of class empl")

    @staticmethod
    def greet():
        print("Good morning!")    

hasaan=empl("Hasaan","Urdu",50000)
print(hasaan.name,hasaan.salary,hasaan.lang  )
# hasaan.getinfo()


