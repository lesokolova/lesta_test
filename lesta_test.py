"""
A module with solving problems for the position of an intern in lesta games
"""

import random
from collections import deque
from typing import Any, List

"""
Вопрос №1

На языке Python написать алгоритм (функцию) определения четности целого числа, который будет аналогичен
нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.

Пример:

def isEven(value):

      return value % 2 == 0
      
isEven
"""


def is_even_second(value: int) -> bool:
    """
    Args:
        value - int
    Returns:
        value - bool
    """
    return value & 1 == 0


def is_even_third(value: int) -> bool:
    """
    Args:
        value - int
    Returns:
        value - bool
    """
    return round(value + 0.5) == value


if __name__ == "__main__":
    print(is_even_second(random.randint(1, 1000)))
    print(is_even_third(random.randint(1, 1000)))

"""
Вопрос №2

На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. 
Объяснить плюсы и минусы каждой реализации.

Оценивается:

Полнота и качество реализации
Оформление кода
Наличие сравнения и пояснения по быстродействию
"""


class MyFIFO:
    """
    MyFIFO - FIFO data processing using the "list" object
    """

    def __init__(self, *initial_queue: Any):
        self.queue = []
        self.queue.extend(*initial_queue)

    def __repr__(self):
        return f"Queue: {self.queue}"

    def __len__(self):
        return len(self.queue)

    def put(self, new_item: Any):
        """
        The function of adding a new item to the queue
        Args:
            new_element - any value
        """
        self.queue.append(new_item)
        print(f"{new_item} added to the queue")

    def pop(self):
        """
        The function removes the first item in the queue
        """
        if self.queue:
            pop_item = self.queue.pop(0)
            print(f"{pop_item} is out of the queue")
        else:
            print('The queue is empty')

    def clear(self):
        """
        Queue clearing function
        """
        self.queue.clear()
        print("The queue is empty")


if __name__ == "__main__":
    first = MyFIFO(['Jackie', 'V', 'Johnny'])
    print(first)
    first.put('Delamain')
    print(first)
    first.pop()
    print(first)
    print(len(first))
    first.clear()
    print(first)


class FIFOQueue:
    """
    FIFOQueue - FIFO data processing using the queue data type (two-way queue)
    """

    def __init__(self, *initial_queue: Any):
        self.queue = deque(initial_queue)

    def __repr__(self):
        return f"Queue: {self.queue}"

    def __len__(self):
        return len(self.queue)

    def enqueue(self, new_item: Any):
        """
        The function of adding a new item to the queue
        Args:
            new_element - any value
        """
        self.queue.append(new_item)
        print(f"{new_item} added to the queue")

    def dequeue(self):
        """
        The function removes the first item in the queue
        """
        if self.queue:
            pop_item = self.queue.popleft()
            print(f"{pop_item} is out of the queue")
        else:
            print('The queue is empty')

    def clear(self):
        """
        Queue clearing function
        """
        self.queue.clear()
        print("The queue is empty")


if __name__ == "__main__":
    first = FIFOQueue(1, 2, 3, {'morning': 'breakfast'}, ['l', 'u', 'c', 'k', 'y'])
    print(first)
    first.enqueue(6)
    print(first)
    first.dequeue()
    print(first)
    print(len(first))
    first.clear()
    print(first)


"""
Вопрос №3

На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) 
отсортирует данный ей массив чисел. 
Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). 
Объяснить, почему вы считаете, что функция соответствует заданным критериям.
"""


def quick_sort(array: List[int]) -> List[int]:
    """
    Takes in any array of numbers, returns an ordered array
    Args:
        array - any list of numbers
    Returns:
        array - ordered array
    """
    if len(array) < 2:
        return array
    if len(array) == 2:
        if array[0] < array[1]:
            return array
        return array[::-1]
    temp = array.pop(len(array) // 2)
    left = []
    right = []
    for i in array:
        if i < temp:
            left.append(i)
        else:
            right.append(i)
    result = quick_sort(left) + [temp] + quick_sort(right)
    return result


if __name__ == "__main__":
    random_array = [random.randint(1, 100) for i in range(10)]
    print(quick_sort(random_array))
