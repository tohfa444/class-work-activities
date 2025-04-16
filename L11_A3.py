n=int(input("Enter your number"))
temp=n
sum=0
while temp>0:
    rem=temp%10
    sum=sum+rem**3
    temp=temp//10
if n==sum:
    print(n," is an armstrong number")
else:
    print(n," is not an armstrong number")