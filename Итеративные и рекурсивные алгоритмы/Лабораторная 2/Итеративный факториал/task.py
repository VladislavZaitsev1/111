def factorial_iterative(n: int) -> int:

    if not isinstance(n, int):
        raise TypeError(f"Факториал может быть найден только для целого положительного числа а не для {type(n)}")
    if n <= 0:
        raise ValueError("Факториал может быть найден только для целого положительного числа")

    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac
     # TODO реализовать итеративный алгоритм нахождения факториала


if __name__ == '__main__':
    print(factorial_iterative(6))

