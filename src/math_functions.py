def factorial(n: int) -> int:
    """Вычисление факториала (итеративно)."""
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n: int) -> int:
    """Вычисление факториала (рекурсивно)."""
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел.")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

def fibo(n: int) -> int:
    """Вычисление числа Фибоначчи (итеративно)."""
    if n < 0:
        raise ValueError("Числа Фибоначчи определены для неотрицательных индексов.")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibo_recursive(n: int) -> int:
    """Вычисление числа Фибоначчи (рекурсивно)."""
    if n < 0:
        raise ValueError("Числа Фибоначчи определены для неотрицательных индексов.")
    if n <= 1:
        return n
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)