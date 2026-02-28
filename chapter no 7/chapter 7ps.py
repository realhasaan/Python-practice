#problem 1
# n=int(input("Enter the number nigga "))
# for i in range (1,11):
#     print(f"{n} * {i} = {n*i}")


#Problem 2

# l=["hasaan","Safura","Sufian","imran"]
# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")


#Problem 3
# n=int(input("Enter the number nigga "))
# i=1
# while(i<=10):
#     print(f"{n} * {i} = {n*i}")
#     i=i+1

#problem 4
# n=int(input("Enter the number nigga "))
# for i in range(2,n):
#     if(n%i)==0:
#         print("Number is not prime")
#         break

# else:
#     print("Numer is prime")    

#problem 5
# i=0
# sum=0
# n=int(input("Enter the number nigga "))
# while(i<=n):
#     sum+=i
#     i+=1

# print(sum) 


#Problem 6
#5!=1x2x3x4x5
# product=1
# n=int(input("Enter the number nigga "))
# for i in range (1,n+1):
#     product=product*i
# print(f"The product of {n} is {product}")

#Problem 7

# Write a program to print the following star pattern.
#  *
# ***
# ***** for n = 3

# n=int(input("Enter the number nigga "))
# for i in range (1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1),end=" ")
#     print("")  
#Problem 8
#  Write a program to print the following star pattern:
# *
# **
# *** for n = 3

# n=int(input("Enter the number nigga "))
# for i in range (1,n+1):
#     print("*"*i,end="")
#     print("")    

#Problem 9

# Write a program to print the following star pattern.
# * * *
# *   *         for n = 3
# * * *

# n=int(input("Enter the number nigga "))
# for i in range (1,n+1):
#     if(i==1 or i==n):
#         print("*"*n)
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="") 
#         print("*",end="")   
#         print("")

#Problem 10
#  Write a program to print multiplication table of n using for loops in reversed
# order.
#using while loop
# n=int(input("Enter the number nigga "))
# i=10
# while(i>=1):
#     print(f"{n} * {i} = {n*i}")
#     i=i-1

# using for loop
n=int(input("Enter the number nigga "))
for i in range (1,11):
    print(f"{n} * {11-i} = {n*(11-i)}")