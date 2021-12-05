from random import randrange
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(quantity = 5, repeat = 'True', *list_jokes):
    if (repeat == 'False') and (quantity > 5):
        quantity = 5

    for q in range(0, quantity):
        for i in range(0, len(list_jokes)):
            random_id = randrange(len(list_jokes[i]))

            #Если повторы включены выводим без удаления, иначе удаляем выведенные значения
            print(list_jokes[i][random_id], end=' ') if repeat != True else \
                print(list_jokes[i].pop(random_id), end=' ')
        print()
repeat = input('Разрешить повторы? (True/False): ')
quantity = int(input('Сколько шуток вывести? (Без повторов максимум 5): '))
print()
get_jokes(quantity, repeat, nouns, adverbs, adjectives)