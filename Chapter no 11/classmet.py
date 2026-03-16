class emp:
    a=2
    @classmethod
    def show(cls):
        print(f"The clas attribute value of a is {cls.a}")

o=emp()
o.a=12
print(f"The value of a is {o.a}")    