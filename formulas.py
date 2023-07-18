forms = []
value = []
naity = []
itog_form = []
vozm_form = []
formulus = ["C = p * b", "C = u / b", "N = i * m"]
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
        value.append(int(count))
    return forms, value



def get_vozm_formulus():
    for string in formulus:
        for char in string:
            if char == "=":
                break
            if char.isalpha and char in naity:
                vozm_form.append(string)
    return vozm_form


def get_itog_formulus():
    get_vozm_formulus()
    for string in vozm_form:
        a = True
        b = False
        for char in string:
            if char == "=":
                b = True
            if b == True:
                if char.isalpha() and char in forms:
                    continue
                elif char.isalpha() and char not in forms:
                    a = False
                    break
        if a == True:
            itog_form.append(string)
    return itog_form


