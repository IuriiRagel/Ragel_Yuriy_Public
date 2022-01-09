N=int(input("Enter tickets quantity "))
Age=[int(input(f"enter age for guest {i+1} ")) for i in range (N)]

price = 0
for age in Age:
    if age > 25:
        price += 1390
    elif age > 18:
        price += 990
    else:
        price += 0 # free
if N > 3:
    price= price * 0.9
    print(f"your total price for {N} people with 10% discount is {price}")
else:
    print(f"your total price for {N} people is {price}")



