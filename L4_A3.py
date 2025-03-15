#take marks as input from users
print("Enter the marks obtaind of three subjects")
math=int(input("Enter your math's marks"))
science=int(input("Enter your science's marks"))
english=int(input("Enter your english's marks"))

#Let's calculate the percentage of marks
sum_=math+english+science
print("sum of maths, science, english is ")
percentage=(sum_/300)*100
print(end="percentage mark=")
print(percentage)