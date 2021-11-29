first_list = []

for i in range(1, 1001):
    if i % 2 != 0:
        number = i**3
        first_list.append(number)

print(first_list)


def sum_num(additional_number):
    sum_number_list = 0
    i = 0
    while i < len(first_list):
        number = first_list[i] + additional_number
        sum_number = 0
        while number != 0:
            sum_number += number % 10
            number //= 10

        if sum_number % 7 == 0:
            sum_number_list += first_list[i]
        i += 1

    print('a)', sum_number_list)

sum_num(0)
sum_num(17)