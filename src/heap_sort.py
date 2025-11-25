from typing import List

def heap_sort(arr: List[int]) -> List[int]:
    n = len(arr)

    def _heapify(items, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and items[l] > items[largest]:
            largest = l
        if r < n and items[r] > items[largest]:
            largest = r
        if largest != i:
            items[i], items[largest] = items[largest], items[i]
            _heapify(items, n, largest)

    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0)
    
    return arr