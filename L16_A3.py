p=int(input("enter the first number"))
q=int(input("enter the second number"))
n=input("What do you want to do with these number \nAdditin \nsubstraction \nmultiplication \ndivition\n")
def addition():
    r1=(p+q)
    print(p,"+",q,"=",r1)
    return(r1)

def substraction():
    r2=(p-q)
    print(p,"-",q,"=",r2)
    return(r2)

def multiplication():
    r3=(p*q)
    print(p,"x",q,"=",r3)
    return(r3)

def divition():
    r4=(p/q)
    print(p,"/",q,"=",r4)
    return(r4)

if  n=="addition":
    addition()
elif  n=="substraction":
    substraction()
elif  n=="multiplication":
    multiplication()
else:
    divition()

