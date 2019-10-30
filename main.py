import os_func
import bank_func
import victory_func

while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')

    choice = input('Выберите пункт меню')
    if choice == '1':
        os_func.create_dir(input('Введите наименование создаваемой папки'))

    elif choice == '2':
        os_func.remove_dir_file(input('Введите наименование папки/файла для удаления'))

    elif choice == '3':
        name_src = input('Введите наименование старого файла/папки для копирования')
        name_dst = input('Введите наименование нового файла/папки для копирования')
        os_func.copy_dir_file(name_src, name_dst)

    elif choice == '4':
        for i in os_func.get_dir_file():
            print(i)

    elif choice == '5':
        for i in os_func.get_dir():
            print(i)

    elif choice == '6':
        for i in os_func.get_file():
            print(i)

    elif choice == '7':
        print(os_func.get_info_os())

    elif choice == '8':
        os_func.info_author()

    elif choice == '9':
        victory_func.victory()

    elif choice == '10':
        bank_func.bank_account()

    elif choice == '11':
        os_func.change_wd(input('Введите наименование папки/файла для удаления'))

    elif choice == '12':
        break

    else:
        print('Неверный пункт меню')
