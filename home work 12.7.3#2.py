per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=int(input("enter deposit amount"))
deposit=[]
for i in per_cent:
    deposit.append(money*per_cent[i]/100)
print("Максимальная сумма, которую вы можете заработать",max(deposit))
print(deposit)