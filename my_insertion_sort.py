
count = 0

def my_insertion_sort(iter_list):
  def swap(iter_list):
    for num in range(1, len(iter_list)):
      global count
      count += 1
      if iter_list[num] < iter_list[num-1]:
        iter_list[num], iter_list[num-1] = iter_list[num-1], iter_list[num]
        reverse_swap(iter_list, 1, num)
  def reverse_swap(iter_list, start, stop):
    global count
    for num in range(stop-1, start-1, -1):
      count += 1
      if iter_list[num] < iter_list[num-1]:
        iter_list[num], iter_list[num-1] = iter_list[num-1], iter_list[num]
      else:
        break

 
  swap(iter_list)
  return(iter_list, count)