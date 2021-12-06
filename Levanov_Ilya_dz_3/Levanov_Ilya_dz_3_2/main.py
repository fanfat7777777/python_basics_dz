t_num = {"zero":"ноль",
               "one":"один",
               "two":"два",
               "three":"три",
               "four":"четыре",
               "five":"пять",
               "six":"шесть",
               "seven":"семь",
               "eight":"восемь",
               "nine":"девять",
               "ten":"десять"}

def num_translate_adv():
    num = input('Введите на английском число от 0 до 10: ')
    res = None
    for k, v in t_num.items():
        if k == num:
            res = v
        elif k.title() == num:
            res = v.title()
    return res




print(num_translate_adv())