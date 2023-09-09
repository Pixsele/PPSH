from my_calc import *

cont = 1
correct = True
while cont == 1:
    while correct == True:
        try:
            a = int(input('Введите первое число выражения : '))
            b = int(input('Введите второе число выражения : '))
            correct = False
        except ValueError:
            print('Введите число!')
            correct = True
    print('Выберите математическую операцию из списка')
    print('1 - Сложение\n2 - Вычетание\n3 - Умножение\n4 - Деление')
    operation = input('Введите её номер : ')
    
    if operation == '1':
        answer = add(a,b)
    elif operation == '2':
        answer = subtract(a,b)
    elif operation == '3':
        answer = multiply(a,b)
    elif operation == '4':
        answer = divide(a,b)
    else:
        raise ValueError('Некорректная операция')
    
    print(f'Результат выражения = {answer}')
    print('Хотети продолжить?\nНажмите:\n1 - для продолжения\n2 - для выхода')
    cont = int(input())
    correct = True
    