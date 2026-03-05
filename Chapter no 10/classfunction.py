class empl:
    lang="English"   #class attribute 
    slary=50000
    def getinfo(self):
        print(f"Language: {self.lang}, Salary: {self.slary}")
    @staticmethod
    def greet():
        print("Good morning!")    
hasaan=empl()
hasaan.greet()
hasaan.getinfo()


