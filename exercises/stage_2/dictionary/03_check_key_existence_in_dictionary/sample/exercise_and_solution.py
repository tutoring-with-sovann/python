# Create a dictionary called 'country_capitals' with at least three countries as keys and their capitals as values
# Choose a key to check if it exists in the dictionary (for example 'Japan')
# Use an if statement to check if the key exists
# If it exists print "Yes, the key exists"
# Otherwise print "No, the key does not exist"

country_capitals = {
"Cambodia": "Phnom Penh",
"Thailand": "Bangkok",
"Vietnam": "Hanoi"
}

key_to_check = "Japan"

if key_to_check in country_capitals:
  print("Yes, the key exists")
else:
  print("No, the key does not exist")
