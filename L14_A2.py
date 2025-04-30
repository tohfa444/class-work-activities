print("Hulf piramid paterns of stars is ")
n=int(input("Enter the number of the raws"))
i=0
count=1
while i<=n:
    i+=1
    for j in range(1,i):
        print(count,end=" ") 
        count+=1
    print()
