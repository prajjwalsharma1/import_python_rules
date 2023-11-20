
a=7
def h():
    global a
    a=5
    print(a)
h()


def f2():
    print(a)

f2()

print(globals())
print(dir())