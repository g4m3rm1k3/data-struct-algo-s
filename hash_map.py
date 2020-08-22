class AlgoHashTable:
  '''hash table function instantiate size'''
  def __init__(self, size):
    self.size = size
    self.hash_table = self.create_buckets()

    
  # FUNCTION TO CREAT BUCKETS
  def create_buckets(self):
    return [[] for _ in range(self.size)]

  # SET OR UPDATE VALUES
  def set_val(self, key, value):
    hashed_key = hash(key)%self.size
    bucket = self.hash_table[hashed_key]
    found_key = False
    for index, record in enumerate(bucket):
      record_key, record_value = record
      if record_key == key:
        found_key = True
        break
    if found_key:
      bucket[index] = (key, value)
    else:
      bucket.append((key, value))

  # RETRIEVE VALUES
  def get_val(self, key):
    hashed_key = hash(key)%self.size
    bucket = self.hash_table[hashed_key]
    found_key = False
    for index, record in enumerate(bucket):
      record_key, record_value = record
      if record_key == key:
        found_key = True
        break
    if found_key:
      return record_value
    else:
      return f"{key} not found"

  # REMOVE VALUES
  def delete(self, key):
    hashed_key = hash(key)%self.size
    bucket = self.hash_table[hashed_key]
    self.hash_table.pop(hashed_key)
    found_key = False
    for index, record in enumerate(bucket):
      record_key, record_value = record
      if record_key == key:
        found_key = True
        break
    if found_key:
      self.hash_table.pop(hashed_key)
    else:
      return f"{key} not found"

      
  # RETURN VALUES
  def __str__(self):
    return "".join(str(item) for item in self.hash_table if item)

