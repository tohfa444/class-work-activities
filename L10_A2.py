#input a word or sentence
string=input("Please enter your own string")
string2=""
for i in string:
    string2=i+string2
#   print(string2)
print("The original string is ",string)
print("reverse string is ",string2)