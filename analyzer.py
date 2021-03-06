from time import time
from random import randint
from demos import *
def create_random_list(size, max_val):
  return [randint(1, max_val) for num in range(size)]


size  = int(input("What size list do you want to create: "))
max = int(input("What is the max value of the range: "))
runs = input("How many times do you want to run the function: ") or 0
skip = input("Enter functions to skip: ") or None
print('\n\n\n')

if skip:
  skip = eval(skip)

l = create_random_list(size, max)

def check_o(size, max, runs = 1, *args):
  functions = [quicksort,mergesort,bubble, selection_sort, insertion_sort, sorted]

  for function in functions:

    if function in args:
      print(f"Skipping {function.__name__ + '.'*3}")

    else:
      l = create_random_list(size, max)
      start = time()
      function(l)
      end = time()
      name = f"{function.__name__.capitalize() + '.'*(20-(len(function.__name__)))}\tTime elapsed = {end - start:.5f}"
      print(name)
  while runs > 1:
    print(f"{runs-1} more {''.join(['runs' if runs > 2 else'run'])} \n{'-' * (len(name)+3)} \n")
    return check_o(size, max, runs-1, args)

check_o(size, max, int(runs), skip)

