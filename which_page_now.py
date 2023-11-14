# 75->
# 142->
def h(name):
    print(name)
h(name="prajjwal") # nam and name will be same
#We can use both positional and keyword arguments simultaneously. But first we have to
#take positional arguments and then keyword arguments,otherwise we will get 
# default argument 
def h(name="hello"):
    print(name)
h() # if we dont have argument then it will take default argument