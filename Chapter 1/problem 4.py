import os

# specify the path you want to list
path = "/"  # change this to any directory you want

try:
    contents = os.listdir(path)  # get list of directory contents
    print(f"Contents of '{path}':")
    for item in contents:
        print(item)  # print each file/folder
except FileNotFoundError:
    print("The directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")