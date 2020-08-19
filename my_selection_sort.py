def selection_sort(iter_nums):
  swap = True
  marker = 0
  count = 0
  while swap:
    swap = False
    marker += 1
    for idx, num in enumerate(iter_nums[marker:]):
      if iter_nums[idx+marker] < iter_nums[marker-1]:
        count += 1
        iter_nums[idx+marker], iter_nums[marker-1] = iter_nums[marker-1], iter_nums[idx+marker]
        swap = True
  return(iter_nums, count)
    

l1 = [2,10,8,5,3,1,9,6,4,7,]
print(selection_sort(l1))