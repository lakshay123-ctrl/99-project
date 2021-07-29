import os
import shutil
path = "/Users/lenovo/desktop"
print("your files")
print(os.listdir(path))
source = input("enter the source file:-")
destination = input("where to backup:-")
dest = shutil.copy(source,destination)
print("backup successful")
print(os.listdir(path))