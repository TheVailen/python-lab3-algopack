import argparse
import time
from typing import Dict, List, Callable, Any
import sys
import random

from src.math_functions import factorial, fibo
from src.test_generators import rand_int_array
from src.benchmarks import benchmark_sorts
from src.bubble_sort import bubble_sort
from src.quick_sort import quick_sort
from src.heap_sort import heap_sort
from src.counting_sort import counting_sort
from src.radix_sort import radix_sort
from src.bucket_sort import bucket_sort
from src.data_structures import Stack, Queue

try:
    sys.setrecursionlimit(2500)
except RecursionError:
    pass

COMMANDS: Dict[str, Callable[..., Any]] = {
    "bubble_sort": bubble_sort,
    "quick_sort": quick_sort,
    "heap_sort": heap_sort,
    "counting_sort": counting_sort,
    "radix_sort": radix_sort,
    "bucket_sort": bucket_sort,
    "factorial": factorial,
    "fibo": fibo,
}


def demo_math_functions():
    """Демонстрация функций факториала и Фибоначчи."""
    print("--- Математические функции ---")
    print(f"Факториал 5: {factorial(5)}")
    print(f"Фибоначчи 8: {fibo(8)}")

def demo_data_structures():
    """Демонстрация работы стека и очереди."""
    print("\n--- Структуры данных ---")
    s = Stack()
    s.push(10)
    s.push(5)
    s.push(12)
    print(f"Стек (len): {len(s)}")
    print(f"Стек (Peek): {s.peek()}")
    print(f"Стек (Min): {s.min()}")
    s.pop()
    s.pop()
    print(f"Стек (Min после pop): {s.min()}")
    
    print("\n--- Очередь ---")
    q = Queue()
    q.enqueue(20)
    q.enqueue(30)
    print(f"Очередь (Front): {q.front()}")
    print(f"Очередь (Dequeue): {q.dequeue()}")


def demo_sort_benchmark():
    """Демонстрация бенчмарка."""
    N = 1000
    
    print(f"\n--- БЕНЧМАРК 1: Сортировки целых чисел (N={N}) ---")
    
    int_arrays = {
        "Random Int": rand_int_array(0, 10000, N),
        "Reversed Int": [N - i for i in range(N)],
    }
    
    int_algos: Dict[str, Callable[[List[int]], List[int]]] = {
        "Bubble Sort": bubble_sort,
        "Quick Sort": quick_sort,
        "Heap Sort": heap_sort,
        "Counting Sort": counting_sort,
        "Radix Sort": radix_sort,
    }
    
    try:
        int_results = benchmark_sorts(int_arrays, int_algos) 
        
        print("\nРезультаты Integer Benchmark (время в секундах):")
        for algo_name in int_algos.keys():
            print(f"\n{algo_name}:")
            for array_name in int_arrays.keys():
                t = int_results[array_name].get(algo_name, 'N/A')
                print(f"  {array_name}: {t:.6f}")
    except TypeError as e:
        print(f"Ошибка при Integer Benchmark: {e}")

    print(f"\n--- БЕНЧМАРК 2: Сортировки чисел Float [0, 1) (N={N}) ---")

    float_array = [random.random() for _ in range(N)]
    
    float_arrays = {
        "Random Float [0, 1)": float_array,
    }
    float_algos: Dict[str, Callable[[List[float]], List[float]]] = {
        "Bucket Sort": bucket_sort,
        "Quick Sort (Float)": quick_sort, 
    }

    try:
        float_results = benchmark_sorts(float_arrays, float_algos)
        
        print("\nРезультаты Float Benchmark (время в секундах):")
        for algo_name in float_algos.keys():
            print(f"\n{algo_name}:")
            for array_name in float_arrays.keys():
                t = float_results[array_name].get(algo_name, 'N/A')
                print(f"  {array_name}: {t:.6f}")
    except TypeError as e:
        print(f"Ошибка при Float Benchmark: {e}")


def run_demo():
    demo_math_functions()
    demo_data_structures()


def run_benchmarks():
    demo_sort_benchmark()


def interactive_mode():
    print("\n--- Интерактивный режим (CLI). Введите 'exit' для выхода. ---")
    print(f"Доступные команды: {', '.join(COMMANDS.keys())}")
    while True:
        try:
            user_input = input("> ").strip()
            if user_input.lower() == 'exit':
                break
            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0]
            args = parts[1:]

            if command in COMMANDS:
                func = COMMANDS[command]
                
                if command.endswith('_sort'):
                    if command == 'bucket_sort':
                        numbers = [float(x) for x in args]
                    else:
                        numbers = [int(x) for x in args]
                    
                    result = func(numbers)
                    print(result)
                
                elif command in ['factorial', 'fibo']:
                    if len(args) != 1:
                        print(f"Ошибка: Команда '{command}' принимает ровно один аргумент (целое число).")
                        continue
                    
                    n = int(args[0])
                    result = func(n)
                    print(result)

            else:
                print(f"Ошибка: Команда '{command}' не найдена.")

        except ValueError:
            print("Ошибка ввода: Убедитесь, что вы вводите команду и правильные типы чисел (целые или float).")
        except TypeError as e:
            print(f"Ошибка типа данных: {e}")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Демонстрация и бенчмарк алгоритмов сортировки и структур данных. Используйте флаги для выбора режима."
    )
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '--benchmarks',
        action='store_true',
        help='Запустить только сравнительный анализ сортировок.'
    )
    group.add_argument(
        '--demo',
        action='store_true',
        help='Запустить только демонстрацию структур данных и математических функций.'
    )
    group.add_argument(
        '--cli',
        action='store_true',
        help='Запустить интерактивный режим (REPL) для тестирования функций.'
    )

    args = parser.parse_args()

    if args.cli:
        interactive_mode()
    elif args.benchmarks:
        run_benchmarks()
    elif args.demo:
        run_demo()
    else:
        run_demo()
        run_benchmarks()


if __name__ == '__main__':
    main()