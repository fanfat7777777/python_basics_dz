# first_list = []
#
# for i in range(1, 1001, 2):
#     first_list.append(i ** 3)
#
# print(first_list)
#
#
# def sum_num(additional_number):
#     sum_number_list = 0
#     for num in first_list:
#         number = num + additional_number
#         sum_number = 0
#         while number != 0:
#             sum_number += number % 10
#             number //= 10
#
#         if sum_number % 7 == 0:
#             sum_number_list += num
#     print('a)', sum_number_list)
#
# sum_num(0)
# sum_num(17)

#упрощение после просмотра выполненных ДЗ

#То к чему стоит стремиться:
def sum_numbers(value):
    result = 0

    while value != 0:
        result += value % 10
        value //= 10

    return result

cub_my = [i**3 for i in range(1, 1001, 2)]

result_a = sum(filter(lambda num: sum_numbers(num) % 7 == 0, cub_my))
result_b = sum(filter(lambda num: sum_numbers(num + 17) % 7 == 0, cub_my))

print(result_a)
print(result_b)