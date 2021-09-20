# Py Practice
x = 300


def myfunc():
    global x
    # x is called from myfunc to be printed overriding
    # the original variable x = 300
    x = 200


myfunc()

print(x)
