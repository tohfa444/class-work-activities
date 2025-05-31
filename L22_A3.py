lst=[1,8,3,4,6,5,9,2,7,10]
sum=0
for i in lst:
    sum+=i
print(sum)
avg=sum/len(lst)
print(avg)   
lst.sort()
print(lst) 
print(lst[0]," ",lst[-1])
