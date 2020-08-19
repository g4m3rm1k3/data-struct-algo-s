# from random import randint
import operator

# l1 = [randint(1,100) for i in range(100)]
# print(sorted(l1))
def bubble(sorted_list, reverse=False):
  if reverse:
    direction = operator.le
  else:
    direction = operator.ge
  amount = len(sorted_list)
  counter = 0
  for i in range(len(sorted_list)-1):
    swap = False
    amount -= 1
    for i in range(amount):
      counter += 1
      if direction(sorted_list[i], sorted_list[i+1]):
        sorted_list[i], sorted_list[i+1] = sorted_list[i+1], sorted_list[i]
        swap = True
    if swap == False:
      return sorted_list, counter
  return sorted_list, counter
# print(bubble(l1))

# def bubble(sorted_list):
#   amount = len(sorted_list)-1
#   counter = 0
#   for i in range(len(l1)-1):
#     swap = False
#     for i in range(amount):
#       counter += 1
#       if sorted_list[i] > sorted_list[i+1]:
#         sorted_list[i], sorted_list[i+1] = sorted_list[i+1], sorted_list[i]
#         swap = True
#     if swap == False:
#       return sorted_list, counter
#   return sorted_list, counter

    

