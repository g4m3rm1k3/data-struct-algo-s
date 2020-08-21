import operator

def bubble(sorted_list, reverse=False):
  if reverse:
    direction = operator.le
  else:
    direction = operator.ge
  amount = len(sorted_list)

  for i in range(len(sorted_list)-1):
    print(sorted_list)
    swap = False
    amount -= 1

    for i in range(amount):

      if direction(sorted_list[i], sorted_list[i+1]):
        sorted_list[i], sorted_list[i+1] = sorted_list[i+1], sorted_list[i]
        swap = True
    if swap == False:
      return sorted_list
  return sorted_list,


    

