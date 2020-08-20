from random import randint
from my_selection_sort import my_selection_sort
# from my_bubble_sort import bubble
# from course_bubble_sort import bubble_sort
from my_insertion_sort import my_insertion_sort
# l1 = [randint(1,10) for num in range(10)]
l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]  # original case
count = 0
def insertion_sort(arr):
  count = 0
  for key in range(1, len(arr)):
      if arr[key] < arr[key-1]:
        count += 1
        j = key
        print(j)
        while j > 0 and arr[j] < arr[j-1]:
          count += 1
          arr[j], arr[j-1] = arr[j-1], arr[j]
          j -= 1
  print(count)

# print(my_insertion_sort(l))
# insertion_sort(l)
# print(l)