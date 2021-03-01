"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(_list):
    set_number = set()
    for item in _list:
        if item in set_number:
            print('Yes')
        else:
            print('No')
        set_number.add(item)
