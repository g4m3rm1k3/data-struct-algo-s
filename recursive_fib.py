def fib_recur(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
    return fib_recur(n-1) + fib_recur(n-2)

def long_fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    prev = 0
    next = 1
    for i in range(n-1):
      print(f"{prev} + {next} = {prev + next}")
      prev, next = next, prev + next
    return next

# print(long_fib(10))
print(long_fib(1))
# print(long_fib(2))


def fib_runner(z):
  print(f"The {z} number in the fibonacci sequence is {fib_recur(z)}")

z = 0
fib_runner(z)
z = 1
fib_runner(z)
z = 10
fib_runner(z)