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