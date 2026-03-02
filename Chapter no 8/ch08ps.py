#Write a program using functions to find greatest of three numbers.
# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a 
#     elif(b>a and b>c):
#         return b
#     else:
#         return c


# a=12
# b=2
# c=9
# print(f"The greatest of three numbers is: {greatest(a,b,c)}")

#Write a python program using function to convert Celsius to Fahrenheit
# def celtofar(f):
#     c=(f-32)*5/9
#     return c
# f=int(input("Enter the temperature in Fahrenheit: "))
# print(round(celtofar(f),2))


#How do you prevent a python print() function to print a new line at the end.
# print("a")
# print("b")
# print("c",end="")     #give no new line
# print("d",end="")


#Write a recursive function to calculate the sum of first n natural numbers.
#sum(n)=sum(n-1)+n

# def sum(n):
#     if (n==1):
#         return 1
#     return sum(n-1)+n
# n=int(input("Enter a number to calculate the sum of first n natural numbers: "))
# print(sum(n))

#  Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

# def pattern(n):
#     if (n==0):
#         return
#     print("*"*n)
#     pattern(n-1)
# pattern(5)    

#Write a python function which converts inches to cms
# def intocm(inch):
#     cm=inch*2.54
#     return cm
# n=int(input("Enter the length in inches: "))
# print(f"The length in centimeters is: {intocm(n)}")

#Write a python function to remove a given word from a list ad strip it at the same time.
# l=["Zeeshan", "Hasaan", "Rohaan", "Ali", "Daniyal","an"]
# def rem(l,word):
#     n=[]
#     for item in l:
#         if not (item == word):
#             n.append(item.strip(word))
            
#     return n

# print(rem(l,"an"))

#Write a python function to print multiplication table of a given number.
def mult(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
print(mult(5))