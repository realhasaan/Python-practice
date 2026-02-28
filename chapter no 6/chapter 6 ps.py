#Problem 1
# a1=int(input("Enter first number : "))
# a2=int(input("Enter second number : "))
# a3=int(input("Enter third number : "))
# a4=int(input("Enter fourth number : "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("A1 is greatest ",a1)
# if(a2>a1 and a2>a3 and a2>a4):
#     print("A2 is greatest ",a2)
# if(a3>a1 and a3>a2 and a3>a4):
#     print("A3 is greatest ",a3)
# if(a4>a1 and a4>a2 and a4>a3):
#     print("A4 is greatest ",a4)

#Problem 2
# m1=int(input("Enter marks 1 : "))
# m2=int(input("Enter marks 2 : "))
# m3=int(input("Enter marks 3 : "))
# total_percentage=(100*(m1+m2+m3))/300
# if ( total_percentage>=40 and m1>=33 and m2>=33 and m3>=33):
#     print("You are pass",total_percentage)

# else:
#     print("Try again next year",total_percentage)

#Problem 3
# p1="Makes a lot of money"
# p2="buy now"
# p3="subscribe this"
# p4="click this "
# msg=input("Enter the comment Nigga ")
# if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
#     print("this comment is a spam")
# else:
#     print("This is not a spam")    

#Problem 4
# username=input("Enter username ")
# if(len(username)<10):
#     print("your username cotains less than 10 characters")

# else:
#     print("your username cotains more than 10 characters")


#Problem 5
# l=["Hasi","Haris","Amna"]
# name=input("Enter name please :")
# if(name in l):
#     print("List contains name",name)

# else:
#     print("Name doesn't exist")


#problem 6
post=input("Enter the post ")
if("Hasaan".lower() in post.lower() ):
    print("This post contains hasaan")
else:
    print("not in post")    