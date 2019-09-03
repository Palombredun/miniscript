import random

array = [random.randint(0,10) for i in range(10)]

def bubble_sort(array):
  for i in range(len(array)):
    for j in range(0, i-1):
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]

print(array)
bubble_sort(array)
print(array)


tri fusion :
import random

array = [random.randint(0,10) for i in range(10)]
