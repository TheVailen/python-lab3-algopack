from typing import List, Optional
from src.bubble_sort import bubble_sort 

def bucket_sort(arr: List[float], buckets: Optional[int] = None) -> List[float]:
    if not arr:
        return arr
    if not all(isinstance(x, (float, int)) and 0 <= x <= 1 for x in arr):
         raise TypeError("Bucket sort реализован для чисел в диапазоне [0, 1].")

    if buckets is None:
        buckets = 10
        
    bucket_list = [[] for _ in range(buckets)]
    
    for num in arr:
        index = int(buckets * num) 
        if index == buckets: index -= 1 
        bucket_list[index].append(num)
        
    for bucket in bucket_list:
        bubble_sort(bucket) 
        
    k = 0
    for bucket in bucket_list:
        for num in bucket:
            arr[k] = num
            k += 1
            
    return arr