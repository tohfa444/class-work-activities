n=int(input("Enter your number"))

def cube():
    c=n**3
    return(c)

def check():
    if n%3==0:
        print(cube())
check()