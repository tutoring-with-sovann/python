# Exercise:
# - Create a dictionary of phone_list with 2 key/values
# - Print that dictionary
# - Add another phone contact to the dictionary using the 'update' method
# - Print that dictionary again

# Solution

# key is name
# value is the phone number related to that name
phone_list = {
  'Thavarak': '+855 12 345 678',
  'Thanak': '+855 19 345 678',
}

print(phone_list)

# add another contact
phone_list.update({ 'Teacher Sovann': '+855 18 12 345 678' })

print(phone_list)