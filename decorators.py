"""
it allows developers to modify the behavior of function or class.
"""

def demo():
    print("hi Ritheesh")
    x = 20
    y = 10
    print(x/y)
demo()
"""
def function1():
    name = "ritheesh"

          #or
    #print(name)

    def function2():
        print(name)
    return function2
output = function1()
output()
output()
output()
"""

def function1(nam):#this function usage
    name = nam

          #or
    #print(name)

    def function2():
        print(name)
    return function2
name1 = function1("Ritheesh")
name1()


def decorator_name(function):
    def output_function():
        print("initial demo")
        return function()
    return output_function


@decorator_name
def demo():
    print("this is demo")
demo()













