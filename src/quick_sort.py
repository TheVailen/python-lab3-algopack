from typing import List

def quick_sort(arr: List[int]) -> List[int]:

    def _partition(items, low, high):
        pivot = items[high]
        i = low - 1
        for j in range(low, high):
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1

    def _quick_sort_recursive(items, low, high):
        if low < high:
            pi = _partition(items, low, high)
            _quick_sort_recursive(items, low, pi - 1)
            _quick_sort_recursive(items, pi + 1, high)

    _quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr