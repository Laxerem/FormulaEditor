import operator
forms = []
value = []
naity = []
itog_form = []
vozm_form = []
formulus = ["C = p * c", "C = u / b", "N = t * y", "J = 10 * (a + b)"]
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
        get_forms = input() # p = 100
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
    #return forms, value



def get_vozm_formulus():
    for string in formulus:
        for char in string:
            if char == "=":
                break
            if char.isalpha() and char in naity:
                vozm_form.append(string)
    #return vozm_form


def get_itog_formulus():
    get_vozm_formulus()
    get_dict()
    for string in vozm_form:
        a = True
        b = False
        for char in string:
            if char == "=":
                b = True
            if b == True:
                if char.isalpha() and char in forms:
                    continue
                if char.isalpha() and char not in forms:
                    a = False
                    break
        if a == True:
            itog_form.append(string)
    bracked = False
    for string in itog_form:
            b = False
            flag_brack = False
            for char in string:
                if char == "=":
                    b = True
                if b == True:
                    if char == "(":
                        bracked = True
                        flag_brack = True
                    if char == ")":
                        flag_brack = False
                    if char in operators and flag_brack == False:
                        operato.append(char)
    if bracked == True:
        bracker = {}
        index_string_brack = 0
        operator_break = []
        itog_brack_index = []
        index_range = 0
        for string in itog_form:
            flag = False
            brack = False
            in_brack = []
            col_form_brack = 0
            col_operators = 0
            index_string_brack += 1
            for char in string:
                vhod = False
                if char == "=":
                    flag = True
                if flag == True:
                    if char == "(":
                        brack = True
                        itog_brack_index.append(index_string_brack - 1)
                        continue
                if flag == True and brack == True:
                    if char.isalpha():
                        col_form_brack += 1
                        vhod = True
                        in_brack.append(char)
                    if char in operator_dict:
                        operator_break.append(char)
                        col_operators += 1
                    if col_form_brack % 2 == 0 and vhod == True:
                        for i in range(1):
                            print(operator_break)
                            print(index_range)
                            bracker[index_range] = str(operator_dict[operator_break[index_range]](dict[in_brack[i]], dict[in_brack[i + 1]]))
                            print(bracker)
                            index_range += 1
                    if char == ")":
                        brack = False
        index_brack_range = 0
        for i in range(len(itog_form)):
            if i == itog_brack_index[index_brack_range]:
                c = itog_form[itog_brack_index[index_brack_range]]
                flag = False
                brack = False
                for char in c:
                    if char == "=":
                        flag = True
                        continue
                    if flag == True:
                        if char == "(":
                            brack = True
                            c = c.replace(char, "")
                            continue
                        if char == ")":
                            brack = False
                            c = c.replace(char, bracker[index_brack_range])
                            continue
                        if brack == True:
                            c = c.replace(char, "")
                index_brack_range += 1
                itog_form[i] = c
        #return itog_form



def get_dict():
    for i in range(len(forms)):
        dict[forms[i]] = value[i]
    #return dict

def get_otvet():
    index = 0
    char_index = 0
    dot = False
    inde = True
    far = 0
    for string in itog_form:
        j = False
        for char in string:
            char_index += 1
            if char == "=":
                j = True
            if j == True:
                if char.isalpha():
                    inde = True
                    print(flag_forms)
                    flag_forms.append(dict[char])
                if char in operator_dict:
                    inde = True
                if char.isdigit() or char == ".":
                    if inde == True:
                        far = len(flag_forms)
                        flag_forms.append(char)
                        inde = False
                        continue
                    flag_forms[far] += char

        for i in range(len(flag_forms)):
            if type(flag_forms[i]) == str:
                if "." in flag_forms[i]:
                    flag_forms[i] = float(flag_forms[i])
                else:
                    flag_forms[i] = int(flag_forms[i])

        len_flag_forms = len(flag_forms) - 1
        for i in range(len_flag_forms):
            flag_forms[0] = operator_dict[operato[0]](flag_forms[0], flag_forms[1])
            del operato[0]
            del flag_forms[1]
        otvet_dict[naity[index]] = flag_forms[0]
        index += 1
        flag_forms.clear()

