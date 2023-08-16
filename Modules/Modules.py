import my_calc

a = int(input('Введите первое число выражения : '))
b = int(input('Введите второе число выражения : '))

print('Выберите математическую операцию из списка')
print('1 - Сложение\n2 - Вычитание\n3 - Умножение\n4 - Деление')
operation = input('Введите её номер : ')

if operation == '1':
    answer = my_calc.add(a,b)
elif operation == '2':
    answer = my_calc.subtract(a,b)
elif operation == '3':
    answer = my_calc.multiply(a,b)
elif operation == '4':
    answer = my_calc.divide(a,b)
else:
    raise ValueError('Некорректная операция')

print(f'Результат выражения = {answer}')
