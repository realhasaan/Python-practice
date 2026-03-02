#Example of a function that calculates the average of three numbers
#Function definition 
def average(): 
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    c=int(input("Enter the third number: "))
    avg=(a+b+c)/3
    print("The average of the three numbers is: ", avg)
    return avg

a=average()        #Function call to calculate the average of three numbers
average()    
average()    

