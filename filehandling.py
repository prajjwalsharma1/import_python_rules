#print("hello_sharma")
#read() To read total data from the file
#read(n)  To read 'n' characters from the file
#readline() To read only one line
#readlines() To read all lines into a list

# file exit or not os.path.isfile(file naname)
import os 
from os import *

#print(os.path.isfile("sum1.py"))
f = open("modules.py","a+")
f.write("hello")