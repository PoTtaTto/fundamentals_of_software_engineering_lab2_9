#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_sum(arr):
    """
    Рекурсивно вычисляет сумму элементов массива.

    Args:
    - arr (list): Массив, для которого вычисляется сумма.

    Returns:
    - int: Сумма элементов массива.
    """
    if len(arr) == 1:  # Базовый случай: если в массиве остался один элемент, возвращаем его
        return arr[0]

    mid = len(arr) // 2  # Находим середину массива
    left_half = arr[:mid]  # Левая половина массива
    right_half = arr[mid:]  # Правая половина массива

    # Рекурсивно вызываем функцию для левой и правой половин массива, затем складываем их суммы
    return calculate_sum(left_half) + calculate_sum(right_half)


if __name__ == '__main__':
    list_ = [0]
    print('Рекурсивная сумма: ', calculate_sum(list_))
    print('Обычная сумма: ', sum(list_))