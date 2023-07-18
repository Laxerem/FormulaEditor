from formulas import get_arrs, get_itog_formulus, forms, value, naity, itog_form, vozm_form


print("Введите количество формул: ", end='')
povtor = int(input())

print("Введите формулы: ")
get_arrs(povtor)

print("Сколько формул найти?")
col_naity = int(input())

print("Найти:")
for i in range(col_naity):
    get_naity = input()
    naity.append(get_naity)
get_itog_formulus()

print(forms)
print(value)
print(naity)
print(vozm_form)
print(itog_form)

