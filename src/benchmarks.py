import time
from typing import List, Callable, Any, Dict
from copy import copy

def time_it(func: Callable[..., Any], *args: Any, **kwargs: Any) -> float:
    """Измерение времени выполнения функции."""
    start_time = time.perf_counter()
    func(*args, **kwargs)
    end_time = time.perf_counter()
    return end_time - start_time

def benchmark_sorts(arrays: Dict[str, List[Any]], algos: Dict[str, Callable]) -> Dict[str, Dict[str, float]]:
    """Сравнение алгоритмов сортировки на разных наборах данных (Без поддержки cmp)."""
    results = {}
    
    for array_name, array in arrays.items():
        results[array_name] = {}
        for algo_name, algo_func in algos.items():
            time_taken = time_it(algo_func, copy(array)) 
            results[array_name][algo_name] = time_taken
            
    return results