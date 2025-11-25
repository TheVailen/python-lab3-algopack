import pytest
from src.math_functions import factorial, factorial_recursive, fibo, fibo_recursive
from src.test_generators import rand_int_array, reversed_sorted
from src.benchmarks import time_it, benchmark_sorts
from src.data_structures import Stack, Queue
from src.bubble_sort import bubble_sort
from src.quick_sort import quick_sort
from src.heap_sort import heap_sort
from src.counting_sort import counting_sort
from src.radix_sort import radix_sort
from src.bucket_sort import bucket_sort
from typing import List, Callable
import time

"Тесты для математических функций"

def test_factorial_correctness():
    """Проверка корректности итеративного и рекурсивного факториала."""
    assert factorial(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial(5) == 120
    assert factorial_recursive(7) == 5040

def test_fibo_correctness():
    """Проверка корректности итеративного и рекурсивного Фибоначчи."""
    assert fibo(0) == 0
    assert fibo_recursive(1) == 1
    assert fibo(7) == 13
    assert fibo_recursive(8) == 21

def test_math_function_errors():
    """Проверка генерации ValueError при передаче отрицательного числа."""
    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(ValueError):
        factorial_recursive(-1)
    with pytest.raises(ValueError):
        fibo(-1)
    with pytest.raises(ValueError):
        fibo_recursive(-1)

"Тесты для структур данных: Stack и Queue"

def test_stack_push_pop_peek():
    """Базовый тест операций push, pop и peek для стека."""
    s = Stack()
    s.push(10)
    s.push(20)
    assert len(s) == 2
    assert s.peek() == 20
    assert s.pop() == 20
    assert s.pop() == 10
    assert len(s) == 0
    with pytest.raises(IndexError):
        s.pop()

def test_stack_min_o1():
    """Проверка корректности O(1) операции min для стека."""
    s = Stack()
    s.push(5)
    s.push(2)
    s.push(10)
    s.push(1)
    assert s.min() == 1
    s.pop()
    assert s.min() == 2
    s.pop()
    s.pop()
    assert s.min() == 5
    s.pop()
    with pytest.raises(IndexError):
        s.min()

def test_queue_enqueue_dequeue_front():
    """Базовый тест операций enqueue, dequeue и front для очереди."""
    q = Queue()
    q.enqueue('A')
    q.enqueue('B')
    assert len(q) == 2
    assert q.front() == 'A'
    assert q.dequeue() == 'A'
    assert q.dequeue() == 'B'
    assert len(q) == 0
    with pytest.raises(IndexError):
        q.dequeue()
        
"Тесты для алгоритмов сортировки"

# Параметризация для всех сортировок, работающих с List[int]
@pytest.mark.parametrize("sort_algo", [
    bubble_sort, quick_sort, heap_sort, counting_sort, radix_sort])
def test_general_sorts_correctness(sort_algo: Callable[[List[int]], List[int]]):
    """Проверка сортировок на небольшом случайном и обратно отсортированном массиве."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    expected = [1, 1, 2, 3, 4, 5, 6, 9]

    # Пропуск тестов для сортировок, не поддерживающих отрицательные/большие числа
    if (sort_algo in [counting_sort, radix_sort] and any(x < 0 for x in arr)):
        pytest.skip(f"{sort_algo.__name__} не подходит для List[int] с такими значениями.")

    assert sort_algo(arr.copy()) == expected

    arr_rev = reversed_sorted(5)
    assert sort_algo(arr_rev) == [1, 2, 3, 4, 5]


# Параметризация для сортировок на больших случайных данных
@pytest.mark.parametrize("sort_algo", [
    bubble_sort, quick_sort, heap_sort, counting_sort, radix_sort
])
def test_sorts_on_large_random_array(sort_algo: Callable[[List[int]], List[int]]):
    """Проверка сортировок на большом случайном массиве (N=1000)."""
    N = 1000
    random_arr = rand_int_array(0, 10000, N)
    expected = sorted(random_arr)

    if sort_algo in [counting_sort, radix_sort] and any(x < 0 for x in random_arr):
        pytest.skip(f"{sort_algo.__name__} не поддерживает отрицательные числа")

    result = sort_algo(random_arr.copy())
    
    assert result == expected
    assert len(result) == N

def test_counting_radix_sorts():
    """Тест для Counting и Radix Sort на дубликатах и больших числах."""
    arr = [50, 2, 9, 50, 2, 30, 5]
    expected = [2, 2, 5, 9, 30, 50, 50]
    
    assert counting_sort(arr.copy()) == expected
    assert radix_sort(arr.copy()) == expected
    
    with pytest.raises(TypeError):
        counting_sort([-1, 2])

def test_bucket_sort_float():
    """Тест для Bucket Sort, работающего с числами float в диапазоне [0, 1)."""
    arr = [0.42, 0.33, 0.17, 0.99, 0.05, 0.42]
    expected = [0.05, 0.17, 0.33, 0.42, 0.42, 0.99]
    
    assert bucket_sort(arr.copy()) == expected
    
    with pytest.raises(TypeError):
        bucket_sort([0.5, 2.0])

"Тесты для бенчмарков и генераторов"

def test_time_it():
    """Проверка корректности измерения времени time_it."""
    def dummy_func(n):
        time.sleep(n)
    
    t = time_it(dummy_func, 0.01)
    assert t >= 0.01

def test_generator_reversed_sorted():
    """Проверка корректности генератора обратно отсортированного массива."""
    assert reversed_sorted(4) == [4, 3, 2, 1]
    
def test_benchmark_structure():
    """Проверка корректности структуры выходных данных benchmark_sorts."""
    arrays = {"Small": [3, 1, 2]}
    algos = {"Bubble": bubble_sort}
    
    results = benchmark_sorts(arrays, algos)
    
    assert "Small" in results
    assert "Bubble" in results["Small"]
    assert isinstance(results["Small"]["Bubble"], float)