my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print(my_list)

for i in range(0, len(my_list)):
    str_list = my_list[i]   #Получаем строку из списка
    str_name = str_list[str_list.rfind(" ") + 1:] # Получаем имя
    print(f'Привет, {str_name.replace(str_name, str_name.capitalize())}!') #Вывод фразы