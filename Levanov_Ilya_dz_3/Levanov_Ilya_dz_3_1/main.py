text_number = {"zero":"ноль",
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

def num_translate():
    num = input('Введите текстом число с 0 до 10 на английском: ')
    print(text_number.get(num))

num_translate()
