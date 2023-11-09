# It is exactly same as set except that it is immutable.
# Hence we cannot use add or remove functions.
list1=["one","two","three"]
list2=["one","two","three"]
print(id(list1))
print(id(list2))
print(list1 is list2) 
print(list1 is not list2)  
print(list1 == list2)  
# r1 is r2 returns True if both r1 and r2 are pointing to the same object 
