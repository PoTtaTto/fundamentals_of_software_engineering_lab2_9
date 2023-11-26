#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit


# Decorator for tail recursion optimization
class TailRecurseException(BaseException):
    def __init__(self, args, kwargs):
        """
        Initializes the TailRecurseException instance.

        Args:
        - args (tuple): Arguments for the function.
        - kwargs (dict): Keyword arguments for the function.
        """
        self.args = args
        self.kwargs = kwargs


def tail_recursive(func):
    def wrapper(*args, **kwargs):
        """
        Wraps a function to simulate tail recursion.

        Args:
        - args: Arguments for the function.
        - kwargs: Keyword arguments for the function.
        """
        while True:
            try:
                return func(*args, **kwargs)
            except TailRecurseException as e:
                args = e.args
                kwargs = e.kwargs
                continue

    return wrapper


@tail_recursive
def factorial(n, accumulator=1):
    """
    Recursive function to calculate factorial.

    Args:
    - n (int): Number for factorial calculation.
    - accumulator (int): Accumulator for intermediate results.

    Returns:
    - int: Factorial of n.
    """
    if n == 0:
        return accumulator
    else:
        raise TailRecurseException((n - 1, n * accumulator), {})


@tail_recursive
def fib(n, a=0, b=1):
    """
    Recursive function to calculate Fibonacci series.

    Args:
    - n (int): Number in the Fibonacci series.
    - a (int): First number in the series.
    - b (int): Second number in the series.

    Returns:
    - int: The n-th Fibonacci number.
    """
    if n == 0:
        return a
    else:
        raise TailRecurseException((n - 1, b, a + b), {})


if __name__ == '__main__':
    # Time evaluation of the functions
    print("Execution time for recursive function factorial:", timeit.timeit(lambda: factorial(20), number=10000))
    print("Execution time for recursive function fib:", timeit.timeit(lambda: fib(20), number=10000))
