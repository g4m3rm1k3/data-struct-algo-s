from random import randint
import demos


def create_random_list(size, max_val):
  return [randint(1, max_val) for num in range(size)]

print(create_random_list(10, 10))
