class Node:
  def __init__(self, key):
    self.data = key
    self.left_child = None
    self.right_child = None

class BSTDemo:
  def __init__(self):
    self.root = None


  def insert(self, key):
    if not isinstance(key, Node):key = Node(key)

    if self.root == None : self.root = key
    else : self._insert(self.root, key)

  def _insert(self, curr, key):
    if key.data > curr.data:
      if curr.right_child == None : curr.right_child = key
      else : self._insert(curr.right_child, key)
    elif key.data < curr.data:
      if curr.left_child == None : curr.left_child = key
      else : self._insert(curr.left_child, key)
    

  def in_order(self):
    self._in_order(self.root)
    print("\n")

  def _in_order(self, curr):
    if curr:
      self._in_order(curr.left_child)
      print(curr.data, end=" ")
      self._in_order(curr.right_child)

  def find_val(self, key):
    return self._find_val(self.root,key)


  def _find_val(self, curr, key):
    if curr:
      if key == curr.data: return True
      elif key < curr.data: return self._find_val(curr.left_child, key)
      else: return self._find_val(curr.right_child, key)
    return False

  def pre_order(self):
    #root, left, right
    self._pre_order(self.root)
    print("\n")

  def _pre_order(self, curr):
    if curr:
      print(curr.data, end=" ")
      self._pre_order(curr.left_child)
      self._pre_order(curr.right_child)
      

  def post_order(self):
    self._post_order(self.root)
    print("\n")

  def _post_order(self, curr):
    if curr:
      self._pre_order(curr.left_child)
      self._pre_order(curr.right_child)
      print(curr.data, end=" ")

  def min_right_subtree(self, curr):
    if curr.left_child == None:return curr
    else:return self.min_right_subtree(curr.left_child)

  def delete_val(self, key):
    return self._delete_val(self.root, None, None, key)

  def _delete_val(self, curr, prev, is_left, key):
    if curr:
      if key == curr.data:
        if curr.left_child and curr.right_child:
          min_child = self.min_right_subtree(curr.right_child)
          curr.data = min_child.data
          self._delete_val(curr.right_child, curr, False, min_child.data)

        elif curr.left_child == None and curr.right_child == None:
          if prev:
            if is_left: prev.left_child = None
            else: prev.right_child = None
          else:
            self.root = None

        elif curr.left_child == None:
          if prev:
            if is_left: prev.left_child = curr.right_child
            else: prev.right_child = curr.right_child
          else:self.root = curr.right_child
        else:

          if prev:
            if is_left: prev.left_child = curr.left_child
            else: prev.right_child = curr.left_child
          else: self.root = curr.left_child
      elif key < curr.data: return self._delete_val(curr.left_child, curr, True, key)
      else: return self._delete_val(curr.right_child, curr, False, key)
    else: return f"{key} not found"



tree = BSTDemo()
tree.insert("F")
tree.insert("C")
tree.insert("H")
tree.in_order()
tree.insert("H")
tree.insert("D")
tree.insert("I")
tree.insert("M")
tree.insert("J")
tree.insert("L")
tree.insert("F")
tree.insert("G")
tree.insert("A")
tree.insert("B")
tree.insert("K")
tree.insert("E")
print(tree.delete_val("C"))
print(tree.delete_val("H"))
tree.in_order()
tree.pre_order()
tree.post_order()
tree.find_val("C")
tree.find_val("Z")
tree.delete_val("Z")
tree.find_val("E")
ditree.delete_val("F")
tree.in_order()