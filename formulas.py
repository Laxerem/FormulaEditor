from Main import forms
forms = []
value = []
naity = []
itog_form = []
formulus = ["C = p * b", "C = u / b"]
char = str


def get_arrs(povtor):
    for i in range(povtor):
        get_forms = input()
        form = ""
        count = ""
        char_index = 0
        while get_forms[char_index] != "=":
            char = get_forms[char_index]
            form += char
            char_index += 1
        forms.append(form.strip())
        while char_index < len(get_forms):
            if get_forms[char_index].isdigit():
                count += get_forms[char_index]
            char_index += 1
        value.append(count)
    return forms, value


def get_formulus(col_naity):
    a = True
    for string in formulus:
        for char in string:
            if char.isalpha and char in forms:
                continue
            else:
                a = False
                break
        if a == True:
            itog_form.append(string)
    return itog_form
