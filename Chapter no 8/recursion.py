#recursion is a technique which call itself
# Example of a recursive function to calculate the factorial of a number 
'''
factorial(1)=1
factorial(2)=2x1
factorial(3)=3x2x1
factorial(4)=4x3x2x1
factorial(n)=n x factorial(n-1)
'''

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of a number is {factorial(n)}")     