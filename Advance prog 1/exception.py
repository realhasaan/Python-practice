# try:
#     a=int(input("Enter a number: "))
#     print(a)
# except Exception as e:
#     print(e)

# a=int(input("Enter a number: "))
# b=int(input("Enter another number: "))
# if(b==0):
#     raise ZeroDivisionError("Denominator cannot be zero.")
# else:  
#     print(f"The division is {a/b} ")

# try with else
# try:
#     a=int(input("Enter a number: "))
#     print(a)
# except Exception as e:
#     print(e)

# else:
#     print('i am inside else') 

#try with finally
def main():
    try:
        a=int(input("Enter a number: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return


    finally:
        print('i am inside finally')

main()