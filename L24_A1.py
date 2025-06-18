student_data={"name":"Tohfa","class":"nine","age":15,"hobby":"playing games","hair_color":"black"}
print(student_data)

print(student_data["name"])

print(student_data.keys())

print(student_data.values())

dict={"id_1":{"name":"sara","class":"five"},
      "id_2":{"name":"David","class":"five"},
      "id_3":{"name":"Oliv","class":"eight"},
      "id_4":{"name":"sara","class":"five"}}
result={}
for key,value in dict.items():
    if value not in result.values():
        result[key]=value
print(result)



