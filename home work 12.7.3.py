per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=int(input("enter deposit amount"))
deposit=[]
TKB=int(per_cent["ТКБ"]*money/100)
deposit.append(TKB)
CKB=int(per_cent["СКБ"]*money/100)
deposit.append(CKB)
VTB=int(per_cent["ВТБ"]*money/100)
deposit.append(VTB)
SBER=int(per_cent["СБЕР"]*money/100)
deposit.append(SBER)
print(deposit)

print("Максимальная сумма, которую вы можете заработать",max(deposit))
