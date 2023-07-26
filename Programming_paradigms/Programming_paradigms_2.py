numbers = [14, 93, 19, 38, 18, 51, 77]


def sum_numbers(numbers):  # функция суммирования
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_numbers(numbers[1:])


def sum_even_numbers(numbers):  # функция суммирования четных чисел
    new_numbers = list(filter(lambda x: x % 2 == 0,
                              numbers))  # создаем на основе входного массива новый массив, содержащий только четные числа
    result = sum_numbers(new_numbers)
    return result


ans = sum_even_numbers(numbers)
print(ans)
