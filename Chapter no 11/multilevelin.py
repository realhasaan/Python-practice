class emp:
    a=12

class emp2(emp):
    b=3

class emp3(emp2):
    c=6

o=emp()
print(o.a)  
# print(o.b)   

o1=emp2()
print(o1.a,o1.b)

o2=emp3()
print(o2.a,o2.b,o2.c)