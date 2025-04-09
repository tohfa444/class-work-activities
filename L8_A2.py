print("Enter a numder (numerator)")
num_n=int(input())
print("Enter a numder (denominator)")
num_d=int(input())
if num_n%num_d==0:
    print(f"{num_n} is divisible by {num_d}")
else:
    print(f"{num_n} is not divisible by {num_d}")