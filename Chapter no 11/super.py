class emp:
    def __init__(self):
        print("This is the constructor of emp class")
    a=12

class emp2(emp):
    def __init__(self):
        print("This is the constructor of emp2 class")
        super().__init__()
    b=3

class emp3(emp2):
    def __init__(self):
        print("This is the constructor of emp3 class")
    c=6


# o=emp()
# print(o.a)  
  

o1=emp2()
print(o1.a,o1.b)

# o2=emp3()
# print(o2.a,o2.b,o2.c)