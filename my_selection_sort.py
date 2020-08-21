def my_selection_sort(iter_nums):
  swap = True
  marker = 0
  count = 0

  while swap:
    print(iter_nums)
    swap = False
    marker += 1

    for idx, num in enumerate(iter_nums[marker:]):
      count += 1

      if iter_nums[idx+marker] < iter_nums[marker-1]:
        iter_nums[idx+marker], iter_nums[marker-1] = iter_nums[marker-1], iter_nums[idx+marker]
        swap = True

  return(iter_nums, count)
  