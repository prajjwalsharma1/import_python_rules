s= lambda n:n+1
print(s(4))
print("prajjwal_sharma")

mul=lambda n,m:n*m
print(mul(7,8))
# Note:
# Lambda Function internally returns expression value and we are not required to write
# return statement explicitly.
# Note: Sometimes we can pass function as argument to another function. In such cases
# lambda functions are best choice.
# We can use lambda functions very commonly with filter(),map() and reduce() functions,b'z
# these functions expect function as argument.

a={}
a['l']=0
if a['l']  <5:
    print("hellosw")
l=[0,5,10,15,20,25,30]
l1=list(filter(lambda x:x*2,l)) # filter filter on true and false 
print(l1) #[0,10,20,30]
l2=list(filter(lambda x:x%2!=0,l))
print(l2) #[5,15,25] 
l=[0,5,10,15,20,25,30]
l1=list(map(lambda x:x*2,l)) # filter filter on true and false 
print(l1) #[0,10,20,30]
l2=list(filter(lambda x:x%2!=0,l))
print(l2) #[5,15,25] 
#We can apply map() function on multiple lists also.But make sure all list should have same
#length.
