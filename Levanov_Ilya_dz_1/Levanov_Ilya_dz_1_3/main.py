for i in range(1, 101):
    if i % 10 == 1 and i != 11:
        print(i, 'процент')
    elif i == 11 or i == 12 or i == 13 or i == 14:
        print(i, 'процентов')
    elif (i % 10 == 2 or i % 10 == 3 or i % 10 == 4) and (i != 12 or i != 13 or i != 14):
        print(i, 'процента')
    else:
        print(i, 'процентов')
