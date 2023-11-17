# every thing in python is object 

# we can pass function as argument
#: filter(function,sequence)
# map(function,sequence)
# reduce(function,sequence)

def decor(wish):
    def inner(name):
        if name=="Sunny":
            print("Hello Sunny Bad Morning")
        else:
            wish(name)
    return inner

@decor
def decor(name):
    print("Hello",name,"Good Morning")

("Durga")
wish("Ravi")
wish("Sun")