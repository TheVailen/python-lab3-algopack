from typing import List

def counting_sort(arr: List[int]) -> List[int]:
    if not arr:
        return arr
    if not all(isinstance(x, int) and x >= 0 for x in arr):
         raise TypeError("Counting sort поддерживает только целые неотрицательные числа.")
    
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
        
    output = []
    for i in range(max_val + 1):
        output.extend([i] * count[i])
        
    arr[:] = output
    return arr