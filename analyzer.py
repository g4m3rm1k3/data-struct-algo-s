from time import time
from random import randint
from demos import *
def create_random_list(size, max_val):
  return [randint(1, max_val) for num in range(size)]


size  = int(input("What size list do you want to create: "))
max = int(input("What is the max value of the range: "))
runs = input("How many times do you want to run the function: ") or 1
skip = input("Enter functions to skip: ") or None
print('\n\n\n')

if skip:
  skip = eval(skip)

l = create_random_list(size, max)

def check_o(size, max, runs = 1, *args):
  functions = [quicksort,mergesort,bubble, selection_sort, insertion_sort]

  for function in functions:

    if function in args:
      print(f"Skipping {function.__name__ + '.'*3}")

    else:
      l = create_random_list(size, max)
      start = time()
      function(l)
      end = time()
      print(f"{function.__name__.capitalize() + '.'*(20-(len(function.__name__)))}\t {end - start}\
 to sort a list {size} long")
  while runs > 0:
    print(f"{runs} more runs... \n\n")
    return check_o(size, max, runs-1, args)

check_o(size, max, int(runs), skip)

