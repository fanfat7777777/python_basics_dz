my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(my_list)

i = 0
while i < len(my_list):
    n = 0
    f = 0
    str_list = my_list[i]               #сохраняем строку в переменную
    for k in range(0, len(str_list)):   #Перебираем строку
        if str_list[k].isdigit():       #Проверяем на число
            n += 1
            f = k
    if n > 0:                           #Есди в строке есть число, вставляем скобки
        my_list.insert(i, '"')
        my_list.insert(i + 2, '"')
        if n == 1:                      #Если число одно, то добавляем 0
            new_str = f"{str_list[:f]}0{str_list[f:]}"
            my_list.pop(i + 1)
            my_list.insert(i + 1, new_str)
        i += 1
    i += 1

print(my_list)

str_list = " ".join(my_list)
print(str_list)