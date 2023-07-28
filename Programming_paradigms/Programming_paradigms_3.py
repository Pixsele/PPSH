numbers = [60, 84, 9, 49, 7, 85, 38]


def sum_even_numbers(numbers):
    result = 0
    for number in numbers:
        if number % 2 == 0:
            result += number

    return result


ans = sum_even_numbers(numbers)
print(ans)