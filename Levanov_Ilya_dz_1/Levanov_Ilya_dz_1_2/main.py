first_list = []

for i in range(1, 1001, 2):
    first_list.append(i ** 3)

print(first_list)


def sum_num(additional_number):
    sum_number_list = 0
    for num in first_list:
        number = num + additional_number
        sum_number = 0
        while number != 0:
            sum_number += number % 10
            number //= 10

        if sum_number % 7 == 0:
            sum_number_list += num
    print('a)', sum_number_list)

sum_num(0)
sum_num(17)

#упрощение после просмотра выполненных ДЗ