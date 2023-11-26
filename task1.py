#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache


def factorial(n):
    """
    Рекурсивно вычисляет факториал числа n.

    Args:
    - n (int): Целое число для вычисления факториала.

    Returns:
    - int: Факториал числа n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fib(n):
    """
    Рекурсивно вычисляет число Фибоначчи для n.

    Args:
    - n (int): Номер числа Фибоначчи.

    Returns:
    - int: Число Фибоначчи.
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def factorial_iterative(n):
    """
    Итеративно вычисляет факториал числа n.

    Args:
    - n (int): Целое число для вычисления факториала.

    Returns:
    - int: Факториал числа n.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fib_iterative(n):
    """
    Итеративно вычисляет число Фибоначчи для n.

    Args:
    - n (int): Номер числа Фибоначчи.

    Returns:
    - int: Число Фибоначчи.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    # Оценка времени выполнения функций
    print("Время выполнения рекурсивной функции factorial:", timeit.timeit(lambda: factorial(20), number=10000))
    print("Время выполнения рекурсивной функции fib:", timeit.timeit(lambda: fib(20), number=10000))
    print("Время выполнения итеративной функции factorial:", timeit.timeit(lambda: factorial_iterative(20), number=10000))
    print("Время выполнения итеративной функции fib:", timeit.timeit(lambda: fib_iterative(20), number=10000))

    # Применение декоратора lru_cache к рекурсивным функциям
    factorial = lru_cache(maxsize=None)(factorial)
    fib = lru_cache(maxsize=None)(fib)

    # Оценка времени выполнения функций с применением lru_cache
    print("Время выполнения рекурсивной функции factorial (с lru_cache):",
          timeit.timeit(lambda: factorial(20), number=10000))
    print("Время выполнения рекурсивной функции fib (с lru_cache):", timeit.timeit(lambda: fib(20), number=10000))
