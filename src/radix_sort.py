from typing import List

def radix_sort(arr: List[int], base: int = 10) -> List[int]:
    if not arr:
        return arr
    if not all(isinstance(x, int) and x >= 0 for x in arr):
         raise TypeError("Radix sort поддерживает только целые неотрицательные числа.")

    max_val = max(arr)
    place = 1
    
    def counting_sort_by_digit(items, place):
        size = len(items)
        output = [0] * size
        count = [0] * base

        for i in range(size):
            index = (items[i] // place) % base
            count[index] += 1

        for i in range(1, base):
            count[i] += count[i - 1]

        i = size - 1
        while i >= 0:
            index = (items[i] // place) % base
            output[count[index] - 1] = items[i]
            count[index] -= 1
            i -= 1

        for i in range(size):
            items[i] = output[i]

    temp_arr = arr
    while max_val // place > 0:
        counting_sort_by_digit(temp_arr, place)
        place *= base
        
    return temp_arr