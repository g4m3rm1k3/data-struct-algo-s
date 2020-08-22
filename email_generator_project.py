from random import choice, shuffle
from string import ascii_lowercase, ascii_uppercase


def gen_string(length=10):
  '''GENERATE A STRING OF RANDOM CHARACTERS GIVEN A LENGTH VALUE'''
  # CREATE A LIST OF LEGAL EMAIL CHARACTERS
  letters = [a for a in ascii_lowercase] +[a for a in ascii_uppercase]\
+[str(num) for num in range(10)]+["_","-","!","#"]
  shuffle(letters)
  # CREATE AN EMPTY LIST TO HOLD THE SEQUENCE
  string_list = []
  # APPEND CHARACTERS
  for i in range(length):
    string_list.append(choice(letters))
  # RETURN LIST OF CHARACTERS
  return string_list

def append_email(email):
  '''CONCAT THE STRING TO THE SUFFIX TO CREATE EMAIL STRING'''
  # LIST OF SUFFIX TO APPEND TO EMAILS
  emails_suffix = ['example.com', 'youtoo.org', 'wtf.co', 'wesuck.gov', 'gmail.com', 'hotmail.com']
  return email + '@' + choice(emails_suffix)

def email_list(amnt,premail="m1k3ymcl34n@gmail.com", length=10):
  '''CREATE A LIST OF EMAILS FROM VALUE amnt premial WILL BE INSERTED'''
  # EMPTY LIST TO HOLD EMAILS
  emails = []
  # LOOP THROUGH amnt TO CREATE EMAILS
  for n in range(amnt):
    # CHECK IF MIDDLE OF LIST TO APPEND PREMAIL
    if amnt//2 == n:
      emails.append(premail)
    # SET email = FUNCTION CALL 
    email = "".join(gen_string(length))
    # APPEND email TO LIST emails
    emails.append(append_email(email))
  return emails


def quicksort(arr):
  """Input: Unsorted list of integers
     Returns sorted list of integers using Quicksort
     Note: This is not an in-place implementation"""

  if len(arr) < 2 :return arr
  else:
    pivot = arr[-1].casefold()
    smaller, equal, larger = [], [], []
    for num in arr:
      if num.casefold() < pivot:smaller.append(num)
      elif num.casefold() == pivot:equal.append(num)
      else: larger.append(num)

    return quicksort(smaller) + equal + quicksort(larger)



def bisection_recur(n, arr, start, stop):
  if start > stop:
    return f"{n} not found in list"
  else:
    mid = (start + stop) // 2
    if n == arr[mid]:
      return f"{n} found at index: {mid}"
    elif n > arr[mid]:
      return bisection_recur(n, arr, mid+1, stop)
    else:
      return bisection_recur(n, arr, start, mid-1)

if __name__ == '__main__':
  pass
