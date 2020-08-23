from math import factorial

class Node:

  def __init__(self, data=None):
    self.data = data
    self.next = None

  def __str__(self):
    return f"{self.data}"

class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None

  def append_val(self, x):
    '''add x to the end of the list'''
    if not isinstance(x, Node):
      x = Node(x)
    if self.head == None: self.head = x
    else: self.tail.next = x
    self.tail = x


  def __str__(self):
    to_print = ""
    current = self.head
    while current is not None:
      to_print += str(current.data) +'->'
      current = current.next
    if to_print:
      return f"[{to_print[:-2]}]"
    return "[]"

  def add_to_start(self, x):
    '''add x to teh left of the list making it the head'''
    if not isinstance(x, Node):
      x = Node(x)
    x.next, self.head = self.head, x
      





  def search_val(self, x):
    '''return indices where x was found'''
    current = self.head
    count = 0
    while current is not None:
      if x == current.data:
        return count
      current = current.next
      count += 1
    return None

  def remove_val_by_index(self, x):
    '''remove and return value at index x provided as paramter'''
    if x == 0:
      self.head = self.head.next
    else:
      current = self.head
      next = current.next
      count = 1
      while next is not None:
        if count == x:
          current.next = next.next
          return current.next
        current = current.next
        next = next.next
        count += 1


        

  def length(self):
    '''return the length of the list, rep'd by number of nodes'''
    count = 0
    current = self.head
    while current is not None:
      current = current.next
      count += 1
    return count

  def reverse_list_recur(self, current, previous=None):
    '''reverse the sequence of node pointers in the linked list'''
    if self.head == None:
       return
    elif current.next == None:
      self.tail = self.head
      current.next = previous
      self.head = current
    else:
      next = current.next
      current.next = previous
      self.reverse_list_recur(next, current)

      
    # code I learned form Geeks for Geeks
    # prev = None
    # current = self.head 
    # while(current is not None): 
    #     next = current.next
    #     current.next = prev
    #     prev = current 
    #     current = next
    # self.head = prev 

# my_list = LinkedList()

# for i in range(10):
#   my_list.append_val(i)

# print(my_list)

# my_list.add_to_start(5)
# my_list.add_to_start(15)
# my_list.add_to_start(35)
# my_list.add_to_start(52)
# print(my_list)
# print(my_list.length())
# print(my_list.search_val(5))
# my_list.remove_val_by_index(my_list.search_val(5))
# my_list.remove_val_by_index(my_list.search_val(5))
# print(my_list.search_val(15))
# print(my_list)
# print(my_list.length())
# print(my_list.reverse_list_recur(my_list.head,None))
# print(my_list)
  