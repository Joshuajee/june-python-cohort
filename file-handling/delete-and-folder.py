import os


#os.remove("img-2024-08-26 10:08:20.454343.jpg")


try:
    os.mkdir("my works")
    print("Folder Created")
except FileExistsError:
    print("Folder Already Exist")