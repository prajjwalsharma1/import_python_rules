from zipfile import *
f=ZipFile("files.zip",'w',ZIP_DEFLATED)
f.write("prajjwal.txt")
f.close()
print("files.zip file created successfully")
from os import *
import os 
c=os.getcwd()
print(c)