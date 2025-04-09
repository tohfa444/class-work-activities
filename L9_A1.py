#take input for the student that he can attend the exam or not
medical_cause=input("Did you have medical cause Y or N")

#Take input of the attendence
atten=int(input("Enter the attendence of the student"))

if medical_cause=="Y":
    print("You are allowed")
else:
    if atten>=75:
        print("you are allowed")
    else:
        print("You are not allowed")




