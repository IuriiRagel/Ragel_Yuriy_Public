N=int(input("Enter tickets quantity "))
price=[]
for i in range(N):
    age=int(input(f"enter age for guest {i+1} "))
    if age>25:
        price.append(1390)
    elif age>18:
        price.append(990)
    else:
        price.append(0)

if N > 3:
    total_price= sum(price) * 0.9
    print(f"your total price for {N} people with 10% discount is {total_price}")
else:
    total_price=sum(price)
    print(f"your total price for {N} people is {total_price}")
