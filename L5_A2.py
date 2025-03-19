#calculate
cost_price=int(input("Enter the cost price of your product"))
selling_price=int(input("Enter the selling price of your product"))
if selling_price>cost_price:
    print("profit")
    profit=selling_price-cost_price
    print(profit)
else:
    print("No profit")