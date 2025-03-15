#Assigning different variables
name="Tohfa"
age=14
is_student=True
weight=42.5

#printing different variables and their datatype
print("name: ",name)
print("datatype of name is: ",type(name))

print("age: ",age)
print("datatype of age is: ",type(age))

print("is_student: ",is_student)
print("datatype of is_student is: ",type(is_student))

print("weight: ",weight)
print("datatype of weight is: ",type(weight))

#type casting to convert the datatype of variables
print("\nafter type casting....")
age=str(age)
print(age)
print("datatype of age is",type(age))

weight=int(weight)
print(weight)
print("datatype of weight is",type(weight))