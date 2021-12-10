tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В'
]

def v_none(it):         #Проверяем и если значения закончились вернём  None
    return klasses[it] if it < len(klasses) else None

for i in range(len(tutors)):
    a = list((tutors[i], v_none(i)) for i in range(len(tutors)))
print('\n', a)