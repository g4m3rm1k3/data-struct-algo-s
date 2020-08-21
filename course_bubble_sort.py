
def bubble_sort(arr):
  swap_happened = True
  count = 0
  while swap_happened:
    print(arr)
    swap_happened = False
    for num in range(len(arr)-1):
      count += 1
      if arr[num] > arr[num + 1]:
        swap_happened = True
        arr[num + 1], arr[num] = arr[num], arr[num + 1]
        # print( arr)
  print(count)


