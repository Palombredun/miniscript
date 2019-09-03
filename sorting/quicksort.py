import random

array = [random.randint(0,20) for i in range(10)]

def partition(A, lo, hi):
  pivot = A[hi]
  i = lo
  for j in range(lo, hi):
    if A[j] < pivot:
      A[i], A[j] = A[j], A[i]
      i += 1
  A[i], A[hi] = A[hi], A[i]
  return i

def quick_sort(A, lo, hi):
  if lo < hi:
    p = partition(A, lo, hi)
    quick_sort(A, lo, p-1)
    quick_sort(A, p+1, hi)

high = len(array)-1
print(array)
quick_sort(array, 0, high)
print(array)
