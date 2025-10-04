# Create two dictionaries: 'dicA' and 'dicB' with some key-value pairs.
# Create an empty dictionary 'dicC' that will store the combined key-value pairs.
# Use a loop to update 'dicC' with the key-value pairs from both 'dicA' and 'dicB'.
# Print the combined dictionary 'dicC' at the end.

dicA = {"name": "Alice", "age": 16}
dicB = {"grade": "10th", "city": "Phnom Penh"}

dicC = {}

for d in (dicA, dicB):
  dicC.update(d)

print(dicC)
