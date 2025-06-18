dict={"codingal":2,"is":2,"best":2,"for":2,"coding":1}
k=2
res=0
for key in dict:
    if dict[key]==k:
        res+=1
print("The frecuency of k is",res)
