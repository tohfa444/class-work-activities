n=int(input("Enter your number to find it's factorials "))
def check(n):
    if n==0:
        return("1")
    elif n<0:
        return("Negative numbers can't have factorials")
    else:
        f=1
        for i in range(n,1,-1): 
            f=f*i
        return(f)
print(check(n))