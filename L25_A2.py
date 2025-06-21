set_x={"green","blue"}
set_y={"blue","yellow"}

set_z=set_x.intersection(set_y)
print(f"intersection of {set_x} and {set_y} is {set_z}")

set_z=set_x.union(set_y)
print(f"union of {set_x} and {set_y} is {set_z}")

set_z=set_x.difference(set_y)
print(f"difference of {set_x} and {set_y} is {set_z}")

set_z=set_y.difference(set_x)
print(f"difference of {set_y} and {set_x} is {set_z}")

set_z=set_y.symmetric_difference(set_x)
print(f"symmetric_difference of {set_y} and {set_x} is {set_z}")