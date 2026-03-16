class number:
    a=1
    b=2
    def __init__(self,n):
        self.n=n

    def __add__(self,num):
        return self.n+num.n    



n=number(4)
m=number(5)
print(n+m)


