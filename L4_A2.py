#taking total amount as input from user
amount=int(input("Please enter amount for withdraw"))

#Calculating the  number of notes of different denominations 
note_1=amount//100
amount%=100
note_2=amount//50
amount%=50
note_3=amount//10
print("Notes of 100 taka ",note_1)
print("Notes of 50 taka ",note_2)
print("Notes of 10 taka ",note_3)
