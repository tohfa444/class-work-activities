import  array as arr

arr_num=arr.array("i",[1,3,5,3,7,9,3])
print(arr_num)

print("number of occurances of the number 3 in the array is ",arr_num.count(3))
print(arr_num[-1::-1])

arr_num.reverse()
print("The reverse order of the array is ",arr_num)

arr=[]

for i in arr_num:
    if i in arr:
        pass
    else:
        arr.append(i)
print(arr)    