import random

# список уникальных ключей = ФИО знаменитости
keys_famous = [
    'Пушкин А.С.',
    'Путин В.В.',
    'Есенин С.А.',
    'Лермонтов М.Ю.',
    'Пелевин В.О.',
    'Питон',
    'Чепмен Г.',
    'Клиз Д.',
    'Гиллиам Т.',
    'Айдл Э.',
    'Джонс Т.',
    'Пейлин М.'
]

# словарь, содержащий дни рождения знаменитостей
dic_famous = {
    'Пушкин А.С.': '06.06.1799',
    'Путин В.В.': '07.10.1952',
    'Есенин С.А.': '03.10.1895',
    'Лермонтов М.Ю.': '15.10.1814',
    'Пелевин В.О.': '22.11.1962',
    'Питон': '20.02.1991',
    'Чепмен Г.': '08.01.1941',
    'Клиз Д.': '27.10.1939',
    'Гиллиам Т.': '22.11.1940',
    'Айдл Э.': '29.03.1943',
    'Джонс Т.': '01.02.1942',
    'Пейлин М.': '05.05.1943'
}

# словарь, содержащий дни прописью
day_famous = {
    '01': 'первого',
    '02': 'второго',
    '03': 'третьего',
    '04': 'четвертого',
    '05': 'пятого',
    '06': 'шестого',
    '07': 'седьмого',
    '08': 'восьмого',
    '09': 'девятого',
    '10': 'десятого',
    '11': 'одиннадцатого',
    '12': 'двенадцатого',
    '13': 'тринадцатого',
    '14': 'четырнадцатого',
    '15': 'пятнадцатого',
    '16': 'шестнадцатого',
    '17': 'семнадцатого',
    '18': 'восемнадцатого',
    '19': 'девятнадцатого',
    '20': 'двадцатого',
    '21': 'двадцать первого',
    '22': 'двадцать второго',
    '23': 'двадцать третьего',
    '24': 'двадцать четвертого',
    '25': 'двадцать пятого',
    '26': 'двадцать шестого',
    '27': 'двадцать седьмого',
    '28': 'двадцать восьмого',
    '29': 'двадцать девятого',
    '30': 'тридцатого',
    '31': 'тридцать первого'
}

# словарь, содержащий месяцы прописью
month_famous = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
}


def trasformation_date(date_arg, month_arg, year_arg):
    return ('{} {} {} года'.format(day_famous.get(date_arg), month_famous.get(month_arg), year_arg))


# декоратор
def add_separator(f):
    def inner_func(*args, **kwargs):
        print('/' * 30)
        res = f(*args, **kwargs)
        print('/' * 30)
        return res

    return inner_func


# применение декоратора
@add_separator
def print_stat(arg_all, arg_true):
    arg_all = int(arg_all)
    arg_true = int(arg_true)
    print("Статистика")
    print("Всего вопросов:", arg_all)
    print("Правильных ответов:", arg_true)
    print("Ошибок:", arg_all - arg_true)
    try:
        print("Процент правильных ответов:", 100 * arg_true / arg_all, '%')
    except ZeroDivisionError:
        print('Результат может Вас испугать, т.к. в знаменателе 0!')


def victory():
    bullvictory = True
    number_question = 0

    while bullvictory:
        counttrue = 0
        countall = 0

        while True:
            try:
                number_question = int(input('Сколько вопросов желаете?'))
                break
            except:
                print('Неверный ввод!')

        for i in range(number_question):
            number_famous = random.sample(range(len(keys_famous)), 1)
            number_famous = int(number_famous[0]) - 1
            born_date = input('Когда родился {}?'.format(keys_famous[number_famous]))
            countall += 1

            if (dic_famous.get(keys_famous[number_famous]) == born_date):
                print('Верно!')
                counttrue += 1

            else:
                print('Ответ неверный!')
                date_true = dic_famous.get(keys_famous[number_famous])[0:2]
                month_true = dic_famous.get(keys_famous[number_famous])[3:5]
                year_true = dic_famous.get(keys_famous[number_famous])[6:10]

                print('{} родился {}'.format(keys_famous[number_famous],
                                             trasformation_date(date_true, month_true, year_true)))

        #вызов декорируемой функции
        print_stat(countall, counttrue)

        bullvictory = input('Желаете еще раз сыграть?(y=Да/Прочее = нет)')

        # использование тернарного оператора
        bullvictory = True if bullvictory == 'y' else False
