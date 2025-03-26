print("enter marks optain in five subjects")
mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())
total=mark1+mark2+mark3+mark4+mark5
average=total/5
if average>=91 and average<=100:
    print("Your grade is A1")
elif average>=81 and average<=90:
    print("Your grade is A2")
elif average>=71 and average<=80:
    print("Your grade is B1")
elif average>=61 and average<=70:
    print("Your grade is B2")
elif average>=50 and average<=60:
    print("Your grade is C1")
elif average>=41 and average<=50:
    print("Your grade is C2")
elif average>=31 and average<=40:
    print("Your grade is D1")
elif average>=0 and average<=31:
    print("Your grade is E1")
else:
    print("invalid input")