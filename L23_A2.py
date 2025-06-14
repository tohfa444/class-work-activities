r=(1,2,3,3,2,1)
def palindrom(r):
    e=len(r)-1
    s=0
    while s<e:
        if r[s]!=r[e]:
            return False
        s+=1
        e-=1
    return True
if palindrom(r):
    print("Tuple is flip flop")
elif palindrom(r):
    print("Tuple is flip flop")
else:
    print("Tuple is not flip flop")

