bill=int(input("The bill is "))
tip=int(input("The tip is "))

def total_cal(bill_amount,tips):
    total=bill_amount+0.01*tips
    total=round(total,2)
    print("The total bill is ",total)
total_cal(bill,tip)
