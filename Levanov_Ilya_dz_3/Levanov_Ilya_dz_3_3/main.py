name = {}

def thesaurus(*names):
    for i in range(0, len(names)):
        k = names[i][:1]
        if k in name:
            v = name[k]
            v.append(names[i])
            name[k] = v
        else:
            name[k] = [names[i]]
    print(name)

thesaurus("Иван", "Мария", "Петр", "Илья")