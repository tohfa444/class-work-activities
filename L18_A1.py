str=input("Enter a string")
for i in range(0,len(str)):
    if str[i]=="A":
        print("A is found")
        break
    else:
        print("A is not found")
