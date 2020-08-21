
def merge_sorted(arr1, arr2):
  print("Merge function called with lists below:")
  print(f"left: {arr1} and right: {arr2}")
  sorted_arr = []
  i, j = 0, 0
  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      sorted_arr.append(arr1[i])
      i += 1
    else:
      sorted_arr.append(arr2[j])
      j += 1
    print(sorted_arr)
  while i < len(arr1):
    sorted_arr.append(arr1[i])
    i += 1
  while j < len(arr2):
    sorted_arr.append(arr2[j])
    j += 1
  return sorted_arr


def divide_arr(arr):
  if len(arr) < 2:
    print(f"Base condition reached with {arr[:]}")
    return arr[:]
  else:
    middle = len(arr)//2
    print("Current list to work with:", arr)
    print("Left split:", arr[:middle])
    print("Right split", arr[middle:])
    l1 = divide_arr(arr[:middle])
    l2 = divide_arr(arr[middle:])
    return(merge_sorted(l1, l2))
    # implied return None


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
# l = [8, 6, 2, 5]
print(divide_arr(l))

# XXXXXXXXXXX PROGRAM EXECUTION XXXXXXXXXX
# l1 = [2,4,6,8,10]
# l2 = [1,3,5,7,8,9]