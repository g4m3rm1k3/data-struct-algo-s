def selection_sort(arr):
  spot_marker = 0
  count = 0
  while spot_marker < len(arr):
    
    for num in range(spot_marker+1,len(arr)):
      count += 1
      if arr[num] < arr[spot_marker]:
        arr[num] , arr[spot_marker]  = arr[spot_marker], arr[num]
    spot_marker += 1
  print(count)