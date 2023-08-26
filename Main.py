import formulas

from formulas import get_arrs, get_itog_formulus, get_otvet, forms, value, naity, itog_form, vozm_form, otvet_dict, operato, dict


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
get_otvet()

print(forms)
print(value)
print(naity)
print(vozm_form)
print(itog_form)
print(operato)
print(dict)
print(otvet_dict)
keys_list = list(otvet_dict.keys())
for i in range(len(keys_list)):
    print("Ответ:", keys_list[i], "=", otvet_dict[keys_list[i]])


