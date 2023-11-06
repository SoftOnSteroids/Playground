'''
Python closure is a nested function that allows us to
access variables of the outer function even after the
outer function is closed.
'''
def counter():
  counter = 1
  def inner_count(delta = 0):
    nonlocal counter
    counter += 1 if delta == 0 else delta
    return counter
  # Return nested function
  return inner_count

# Call outer function and assign it to a variable
count = counter()

# At this point, the execution of the outer function is
# completed, so the 'counter' variable should be destroyed.
# However, when we call the inner_count function using
for _ in range(3):
    print(count())
print("More code here and the state of the variable persist:")
print(count())
# I am able to access the 'counter' variable of the outer function.