name = {}

def thesaurus_adv(*names):
    for i in range(0, len(names)):
        str_name = names[i].split()
        k_surname = str_name[1][:1]    #первая буква фамилии
        k_name = str_name[0][:1]       #Первая буква имени
        if k_surname in name:                            #Если буква Фамилии есть в списке
            if k_name in name[k_surname]:                #Если буква имени тоже есть
                v = name[k_surname][k_name]
                v.append(names[i])
                name.update({k_surname: {k_name: v}})
            else:                                       #Если буква фамилии есть но нет буквы имени
                v = name[k_surname]
                v[k_name] = [names[i]]
                name.update({k_surname: v})
        else:                                           #Нет буквы фамилии и нет буквы Имени
            name.update({k_surname: {k_name: [names[i]]}})
    print(name)
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")