words=["adc","cfc","xyz","kfc","aba","1221"]
count=0
new_l=[]
for i in words:
    if len(i)>2 and i[0]==i[-1]:
        new_l.append(i)
        count+=1
print(count)
print(new_l)