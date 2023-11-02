def my_func():
    x=10       # x is local variable
    print(x)   
my_func()

x=10 # x is local variable
def my_func():
    print(x)
my_func()


x=10
def modify_global():
    global(x)
x=20
modify_global()