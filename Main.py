from formulas import get_arrs, forms, value, naity


print("Введите количество формул: ", end='')
povtor = int(input())

print("Введите формулы: ")
get_arrs(povtor)

print("Сколько формул найти?")
col_naity = int(input())
for i in range(col_naity):
    get_naity = input()
    naity.append(get_naity)

print(forms)
print(value)
print(naity)

