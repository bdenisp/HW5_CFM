import pickle
import os

FILE_NAME = 'base_bank_account.dat'


def save_data(arg_filename, arg_base):
    with open(arg_filename, 'wb') as f:
        pickle.dump(arg_base, f)


def account_inc(base_arg, sum):  # функция пополнения счета (1)
    base_arg[0] += sum
    return base_arg


def buy_operation(base_arg, good_arg, price_arg):  # функция покупки (2)
    if base_arg[0] > price_arg:
        base_arg[0] -= price_arg
        base_arg[1].append(good_arg)
        base_arg[2].append(price_arg)
    else:
        print('Недостаточно денег. Пополните счет.')

    return base_arg


def print_history(base_arg):  # функция печати истории
    for i in range(len(base_arg[1])):
        print('{} -- {}'.format(base_arg[1][i], base_arg[2][i]))


def bank_account():
    base = [0, [], []]  # 0 элемент - счет, 1 элемент - покупки, 2 элемент - цена покупки

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'rb') as f:
            base = pickle.load(f)

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. состояние счета')
        print('5. выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            sum = input('Введите сумму пополнения счета:')
            try:
                sum = int(sum)
                base = account_inc(base, sum)
            except:
                print('Неверный ввод')

        elif choice == '2':
            sum = input('Введите сумму операции:')
            try:
                sum = int(sum)
                operation = input('Наименование операции:')
                base = buy_operation(base, operation, sum)
            except:
                print('Неверный ввод')

        elif choice == '3':
            print_history(base)

        elif choice == '4':
            print(f'Свободный остаток составляет {base[0]} руб.')

        elif choice == '5':
            save_data(FILE_NAME, base)
            break

        else:
            print('Неверный пункт меню')
