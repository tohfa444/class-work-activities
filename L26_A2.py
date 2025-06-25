#set
set_1={1,2,3,}
set_2={"a","b","c"}

set_3=set(zip(set_1,set_2))

print(set_3)

#list
lst_1=[1,2,3,]
lst_2=["a","b","c"]

lst_3=list(zip(lst_1,lst_2))

print(lst_3)


for x,y in zip(lst_1,lst_2[-1::-1]):
    print(x,y)

# dictionary_comprehention
dict={x:y for x,y in zip(lst_1,lst_2)}
print(dict)

# list_comprehention
numbers=[1,2,3,4,5]
even=[x for x in numbers if x%2==0]
print(even)
