<div id="header" align="center">
  <img src="https://media.giphy.com/media/QXwtfadqo7wbfmT46H/giphy.gif" width="100"/>
</div>

---

### Вопрос №1

На языке Python написать алгоритм (функцию) определения четности целого числа, который будет аналогичен
нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.

Пример:

      def isEven(value):
          return value % 2 == 0

Мною приведены две реализации: при помощи логического умножения и использования функции round:

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
          
#### Плюсы:
*- битовая операция может быть более эффективной, чем оператор %, особенно для больших чисел;*
*- нестандартный подход.*
  
#### Минусы:
*- проверка четности при помощью round менее эффективна;*
*- код интуитивно не понятен.*

Выбор реализации зависит от конкретных требований проекта, однако в данном случае приоритет отдается читаемости кода.

---

<div id="header" align="center">
  <img src="https://media.giphy.com/media/fByehYIrOIzO8XolJK/giphy.gif" width="100"/>
</div>

---

### Вопрос №2

На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. 
Объяснить плюсы и минусы каждой реализации.

#### Реализация 1 (использование list): 

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


#### Плюсы:
*- отсутствие импортов;*
*- простота и читаемость кода.*

#### Минусы:
*- удаление элемента из начала списка имеет временную сложность O(n), перенос всех элементов списка не эффективен.*

---

#### Реализация 2 (использование deque):

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

#### Плюсы:
*- использование двусторонней очереди обеспечивает эффективное добавление и удаление элементов;*
*- popleft() имеет константную временную сложность.*

#### Минусы:
*- зависимость от библиотеки.*


Если производительность является ключевым фактором, использование deque предпочтительнее.

---

<div id="header" align="center">
  <img src="https://media.giphy.com/media/JqmupuTVZYaQX5s094/giphy.gif" width="100"/>
</div>

---

### Вопрос №3

На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) 
отсортирует данный ей массив чисел. 
Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). 
Объяснить, почему вы считаете, что функция соответствует заданным критериям.

*QuickSort работает быстрее, чем многие другие алгоритмы сортировки в среднем случае. 
Его средняя временная сложность составляет O(n log n), что делает его эффективным для сортировки больших массивов данных.
Еще лушче QuickSort справляется с частично отсортированными массивами.*
 
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
      
          temp = array[len(array) // 2]
          left = [x for x in array if x < temp]
          centrally = [x for x in array if x == temp]
          right = [x for x in array if x > temp]
      
          return quick_sort(left) + centrally + quick_sort(right)

