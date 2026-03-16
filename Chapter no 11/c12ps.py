#Problem no 1
#1. Create a class (2-D vector) and use it to create another class representing a 3-D vector

# class twodvector:
#      def __init__(self, i, j):
#           self.i=i
#           self.j=j
#      def show(self):
#           print(f"The  2-D vectors are {self.i}i and {self.j}j")

# class threedvector(twodvector):
#         def __init__(self, i, j, k):
#             super().__init__(i,j)
#             self.k=k
#         def show(self):
#             print(f"The 3-D vectors are {self.i}i and {self.j}j and {self.k}k")


# a=twodvector(2,3)
# a.show()
# b=threedvector(2,3,4)
# b.show()    

#problem no 2
# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

# class animals:
#     pass

# class pets(animals):
#     pass

# class dog(pets):
#     @staticmethod
#     def bark():
#         print('Bow Bow')


# d=dog()
# d.bark()


#Problem 3
# Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the value of increment based on the salary.


# class employee:
#     salary = 234
#     increment = 20

#     @property
#     def salaryAfterIncrement(self):
#         return self.salary + self.salary * (self.increment / 100)

#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, salary):
#         self.increment = ((salary / self.salary) - 1) * 100


# e = employee()
# e.salaryAfterIncrement = 280.8
# print(e.increment)

# problem 4
# Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ 

# class complex:
#     def __init__(self,r,i):
#         self.r=r
#         self.i=i

#     def __add__(self,c2):
#         return complex(self.r+c2.r,self.i+c2.i)    

#     def __str__(self):
#         return f"{self.r}+{self.i}i"
    
   
# c1=complex(2,3)
# c2=complex(4,5)
# print(c1+c2)   

#problem 5
# Write a class vector representing a vector of n dimensions. Overload the + and *
# operator which calculates the sum and the dot(.) product of them.

# class Vector:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     # + operator (vector addition)
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y,self.z + other.z)

#     # * operator (dot product)
#     def __mul__(self, other):
#         return (self.x * other.x + self.y * other.y + self.z * other.z)

#     def __str__(self):
#         return f"({self.x}, {self.y}, {self.z})"


# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)

# print("Addition:", v1 + v2)
# print("Dot Product:", v1 * v2)

#  Write __str__() method to print the vector as follows: 7i +8j+10k
class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k


    def __add__(self, other):
        return Vector(self.i + other.i,self.j + other.j,self.k + other.k)

    
    def __mul__(self, other):
        return (self.i * other.i +self.j * other.j +self.k * other.k)


    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 7)

print("Vector 1:", v1)
print("Vector 2:", v2)

print("Sum:", v1 + v2)
print("Dot Product:", v1 * v2)