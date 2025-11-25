import random
from typing import List

def rand_int_array(lo: int, hi: int, n: int, *, distinct: bool = False, seed: int = None) -> List[int]:
    """Генерация случайного массива целых чисел."""
    if seed is not None:
        random.seed(seed)
    
    if distinct:
        if (hi - lo + 1) < n:
            raise ValueError("Невозможно сгенерировать n различных чисел в заданном диапазоне.")
        return random.sample(range(lo, hi + 1), n)
    else:
        return [random.randint(lo, hi) for _ in range(n)]

def list_many_duplicates(n: int, k_unique: int = 5, *, seed: int = None) -> List[int]:
    """Генерация массива с большим количеством одинаковых элементов."""
    if seed is not None:
        random.seed(seed)
    return [random.randint(0, k_unique - 1) for _ in range(n)]

def nearly_sorted(n: int, swaps: int, seed: int = None) -> List[int]:
    """Генерация почти отсортированного массива."""
    if seed is not None:
        random.seed(seed)
    arr = list(range(n))
    for _ in range(swaps):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr  

def reversed_sorted(n: int) -> List[int]:
    """Генерация обратно отсортированного массива."""
    return list(range(n, 0, -1))

def rand_float_array(lo: float, hi: float, n: int, k: float = 0.05, *, seed: int = None) -> List[float]:
    """Генерация случайного массива float."""
    if seed is not None:
        random.seed(seed)
    return [random.uniform(lo, hi) for _ in range(n)]