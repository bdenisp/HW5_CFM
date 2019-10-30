import os
import sys
import shutil


def create_dir(name_dir_arg):
    if not (os.path.exists(name_dir_arg)):
        os.mkdir(name_dir_arg)


def remove_dir_file(name_arg):
    if os.path.exists(name_arg):
        if os.path.isdir(name_arg):
            os.rmdir(name_arg)
        if os.path.isfile(name_arg):
            os.remove(name_arg)
    else:
        print('Ошибочка вышла! Нихт такого файла!')


def copy_dir_file(src_arg, dst_arg):
    if ((os.path.exists(src_arg) and not (os.path.exists(dst_arg)))):
        if os.path.isdir(src_arg):
            shutil.copytree(src_arg, dst_arg)
        if os.path.isfile(src_arg):
            shutil.copy(src_arg, dst_arg)
    else:
        print('Не получится это сделать. Попробуйте еще раз.')


if __name__ == '__main__':
    copy_dir_file('test', 'test_copy')


def get_dir_file():
    return os.listdir()


def get_dir():
    list_dir = []
    for i in os.listdir():
        if os.path.isdir(i):
            list_dir.append(i)
    return list_dir


def get_file():
    list_file = []
    for i in os.listdir():
        if os.path.isfile(i):
            list_file.append(i)
    return list_file


def get_info_os():
    return f'My OS is {sys.platform} ( {os.name} )'


def info_author():
    print('\n*******************************************\n'
          'Консольный файловый менеджер\n'
          'Денис П. Белянин, 2019. Все права защищены.\n'
          '*******************************************\n')


def change_wd(path_arg):
    if not os.path.isabs(path_arg):
        path_arg = os.path.join(os.getcwd(), path_arg)
    return os.chdir(path_arg)
