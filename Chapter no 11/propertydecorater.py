class emp:
    a=2
    @classmethod
    def show(cls):
        print(f"The clas attribute value of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname=value.split()[0]
        self.lname=value.split()[1]
    
o=emp()
o.name="Hasaan Irfan"
print(o.fname,o.lname)
o.a=12
print(f"The value of a is {o.a}")    