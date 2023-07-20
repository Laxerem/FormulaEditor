import operator
forms = []
value = []
naity = []
itog_form = []
vozm_form = []
formulus = ["C = p * b", "C = u / b", "N = t * y"]
operato = []
operators = ["+", "-", "*", "/"]
operator_dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}
flag_forms = []
dict = {}
otvet_dict = {}


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
                if char in operators:
                     operato.append(char)
                if char.isalpha() and char in forms:
                    continue
                if char.isalpha() and char not in forms:
                    a = False
                    break
        if a == True:
            itog_form.append(string)
    return itog_form



def get_dict():
    for i in range(len(forms)):
        dict[forms[i]] = value[i]
    return dict

def get_otvet():
    get_dict()
    j = False
    index = 0
    for string in itog_form:
        for char in string:
          if char == "=":
               j = True
          if char.isalpha() and j == True:
               flag_forms.append(char)
        otvet_dict[naity[index]] = operator_dict[operato[index]](dict[flag_forms[index]], dict[flag_forms[index + 1]])
        flag_forms.clear()
        index += 1
    return otvet_dict

