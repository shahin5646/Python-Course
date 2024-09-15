""" 
  This function takes two lists `keys` and `values` and returns a dictionary where keys and values are paired together.

  Args:
      keys: A list of elements to be used as dictionary keys.
      values: A list of elements to be used as dictionary values.

  Returns:
      A dictionary where keys from the `keys` list are paired with corresponding values from the `values` list.

  Raises:
      ValueError: If the lengths of the two lists are not equal.
   """



def convert_lists_to_dict(keys, values):
 
  # Check if the lengths of the lists are equal
  if len(keys) != len(values):
    raise ValueError("Lengths of keys and values lists must be equal.")

  # Create a dictionary using zip() and dict()
  return dict(zip(keys, values))

# Example usage
K = [1001, 1002, 1003, 1004, 1005]
V = ["USA", "Canada", "China", "Japan", "UK"]

my_dict = convert_lists_to_dict(K, V)
print(my_dict)
