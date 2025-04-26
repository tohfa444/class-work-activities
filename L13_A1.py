string=input("Enter your string ")
char=input("Enter your character ")
i=0
count=0
while(i<len(string)):
    if string[i]==char:
        count+=1
    i=i+1
print(f"Total number of times {char} has occured = {count}")