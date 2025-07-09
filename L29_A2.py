class employee():
     
    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("Destructor called")

def create_obj():
    print("Making Object...")
    obj = employee()
    print("funtion end....")
    return obj

print("Calling Creat_obj() function...")
obj = create_obj()
print("Program end....")