from typing import List, Any
from collections import deque

class Stack:
    
    def __init__(self):
        self._items: List[Any] = []
        self._min_stack: List[Any] = [] 

    def push(self, x: Any):
        self._items.append(x)
        if not self._min_stack or x <= self._min_stack[-1]:
            self._min_stack.append(x)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("pop из пустого стека")
        
        item = self._items.pop()
        
        if item == self._min_stack[-1]:
            self._min_stack.pop()
            
        return item

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("peek из пустого стека")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)

    def min(self) -> Any:
        if not self._min_stack:
            raise IndexError("min из пустого стека")
        return self._min_stack[-1]

class Queue:
    
    def __init__(self):
        self._items = deque() 

    def enqueue(self, x: Any):
        self._items.append(x)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("dequeue из пустой очереди")
        return self._items.popleft() 

    def front(self) -> Any:
        if self.is_empty():
            raise IndexError("front из пустой очереди")
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)