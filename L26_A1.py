num_1=[3,4,7]
num_2=[2,5,9]
result=map(lambda x,y:x+y,num_1,num_2)
print(f"The additon of {num_1} and {num_2} is {list(result)}")

#list
nums=[1,2,3,4,5]
def square(n):
     return n**2
sq=list(map(square,nums))
print(f"squares of numbers in list is {sq}")

#tuple
nums=(1,2,3,4,5)
def square(n):
     return n**2
sq=tuple(map(square,nums))
print(f"squares of numbers in list is {sq}")

#set
nums={1,2,3,4,5}
def square(n):
     return n**2
sq=set(map(square,nums))
print(f"squares of numbers in list is {sq}")
