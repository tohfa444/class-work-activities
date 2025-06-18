country_code={"india":"0091","Austrailia":"0025","Bangladesh":"8801","Nepal":"00977"}

print("country_code for india is",country_code.get("india","notfound"))
print("country_code for Japan is",country_code.get("Japan","notfound"))

squares={1:1,2:4,3:9,4:16,5:25}

print(squares.pop(4))
print(squares)

print(squares.popitem())
print(squares)

try:
    del squares
    print(squares)
except:
    print("the dictionary does not exist")