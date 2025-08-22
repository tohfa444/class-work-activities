#python program to illustrate the use of "is" identity operator
x=44
if (type(x) is int):
    print("true")
else:
    print("false")

x=44.4
if (type(x) is not float):
    print("true")
else:
    print("false") 

x=34
y=34
if (x is y):
    print("X and Y have same identity")

y=35
if (x is not y):
    print("X and Y have differnt identity")
    
