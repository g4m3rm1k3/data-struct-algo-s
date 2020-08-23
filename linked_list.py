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

  def reverse_list_recur(self, current, previous):
    '''reverse the sequence of node pointers in the linked list'''
    current = self.tail
    while current is not None:


  