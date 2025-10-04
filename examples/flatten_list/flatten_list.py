# A flatten list is a one dimensional array(list) that is transformed from a multi dimension array or any nested like array.

# This is a one dimensional array(list).
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# This is a two-dimensional array(matrix).
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# To flatten list in python, we can use the loop to access each array and push each element to a one-dimensional array.
# If the item we target is a `list`, we can recursively pass it as argument to its own function.
# If the item we target isn't `list`, we can append that item into the one-dimensional array we declared.
def flatten_list(target_list, accumulate_list):
  for i in target_list:
    # This is how we check whether a variable is a `list`.
    if type(i) is list:
      accumulate_list = flatten_list(i, accumulate_list)
    else:
      accumulate_list.append(i)

  return accumulate_list;    

# You can see that both `flat_list` and `array` have the same element and is a one-dimensional array.
# The differences is that one is in context that it has been tranformed from a multi-dimensional array, hence we call it *flatten* list.
# The other one you can refer to it as `array` or `list`
flat_list = flatten_list(matrix, [])

print(array)
print(flat_list)