try:
    n1,n2=eval(input("Enter two numbers separated by coma "))
    result=n1/n2
    print("Result is",result)

except ZeroDivisionError as ex:
    print("Exception:",ex)
except SyntaxError as ex:
    print("Exception:",ex)
except NameError as ex:
    print("Exception:",ex)
except ValueError as ex:
    print("Exception:",ex)
except:
    print("Some other error has occured")
else:
    print("No exceptions occured")
finally:
    print("This will execute no matter what")
    