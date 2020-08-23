from linked_list import *

my_list = LinkedList()

for i in range(10):
  my_list.append_val(i)

print(my_list)

my_list.add_to_start(5)
my_list.add_to_start(15)
my_list.add_to_start(35)
my_list.add_to_start(52)
print(my_list)
print(my_list.length())
print(my_list.search_val(5))
my_list.remove_val_by_index(my_list.search_val(5))
my_list.remove_val_by_index(my_list.search_val(5))
print(my_list.search_val(15))
print(my_list)
print(my_list.length())
