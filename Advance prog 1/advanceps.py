# #Problem 1

# try:
#     with open("file 1 .txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:
#     with open("file 2 .txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:    
#     with open("file 3 .txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)
       


#Problem 2
# l=[1,2,3,4,5,8,4]
# for i,item in enumerate(l):
#     if i==2 or i==4 or i ==6:
#         print(item)

#problem 3
# n=int(input("Enter a number: "))
# table=[n*i for i in range(1,11)]
# print(table)


#Problem 4
# try:
#     a=int(input("Enter a number: "))
#     b=int(input("Enter another number: "))
#     print(a/b)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

#Problem 5
n=int(input("Enter a number: "))
table=[n*i for i in range(1,11)]
with open("Table.txt","a") as f:
    f.write(f"Table of {n}: {table}\n")  