def bisection_recur(n, arr, start, stop):
  if start > stop:
    return f"{n} not found in list"
  else:
    mid = (start + stop) // 2
    if n == arr[mid]:
      return f"{n} found at index: {mid}"
    elif n > arr[mid]:
      return bisection_recur(n, arr, mid+1, stop)
    else:
      return bisection_recur(n, arr, start, mid-1)


  # mid = (start + stop) //2
  # if n == arr[mid]:
  #   return f"{n} found at index: {mid} out of {len(arr)}"
  # elif n > arr[mid]:
  #   beg = mid +1
  #   return bisection_recur(n, arr[beg:], 0, len(arr[beg:])-1)
  # elif n < arr[mid]:
  #   end = mid -1
  #   return bisection_recur(n, arr[:end+1], 0, len(arr[:end+1])-1)

def create_list(max_val):
  arr = []
  for num in range(1, max_val+1):
    arr.append(num)
  return arr


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#idx 0  1  2  3  4  5  6  7  8  9
for num in range(1,16):
  print(bisection_recur(num, l, 0, len(l)-1))