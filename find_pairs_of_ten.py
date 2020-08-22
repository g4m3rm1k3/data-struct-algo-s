from random import randint
list_in = [randint(1,10) for i in range(100)]
new_list = []
def find_pairs_of_ten(pairs):
  for i in range(0,((len(pairs)-1))):
    if len(pairs) <= i:
      return find_pairs_of_ten(list_in)
    sum = 10 - pairs[i]
    if sum in pairs:
      if sum == pairs[i]:
        if pairs.count(sum) > 1:
          new_list.append((pairs.pop(i), sum))
          pairs.remove(sum)
        else:
          continue
      else:
        new_list.append((pairs.pop(i), sum))
        pairs.remove(sum)
  return new_list


print(find_pairs_of_ten(list_in))

print(list_in)