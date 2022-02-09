per_cent = {'RBC': 5.6, 'TD': 5.9, 'CIBC': 4.28, 'Scotiabank': 4.0}
money=int(input("enter deposit amount"))
deposit=[]
for i in per_cent:
    deposit.append(money*per_cent[i]/100)
print("Maximum amount that you can earn is",max(deposit))
print(deposit)
