#take input of number of unite consumed from the user
units=int(input("Please enter the number of unites you consumed"))

#check for unites less then 50
if units<50:
    amount=units*2.60
    tax=25

#check for units less the hundrad
elif units<100:
    amount=50*2.60+(units-50)*3.25
    tax=35

#check for units less the two hundrad
elif units<200:
    amount=50*2.60+50*3.25+(units-100)*5.26
    tax=45

#check for units greater than the two hundrad
else:
    amount=50*2.60+50*3.25+100*5.26+(units-200)*8.45
    tax=75

total_amount=amount+tax
print("\nelectricity bill=%.2f"%total_amount)
