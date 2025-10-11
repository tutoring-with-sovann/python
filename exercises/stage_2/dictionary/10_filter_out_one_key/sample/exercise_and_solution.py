classA = {
  "Alice": 85,
  "Bob": 72
}

classB = {
  "Charlie": 90,
  "Dara": 88
}

# Combine both dictionaries

all_scores = {}
for d in (classA, classB):
  all_scores.update(d)

print("All student scores:", all_scores)

# Ask for a student name and check if it exists

name_to_check = input("Enter a student name to remove: ")

if name_to_check in all_scores:
  del all_scores[name_to_check]
  print(name_to_check, "was removed.")
else:
  print("Student not found.")

print("Updated scores:", all_scores)

# Find top and lowest students

if all_scores:  # make sure dictionary is not empty
  top_student = max(all_scores.keys(), key=all_scores.get)
  lowest_student = min(all_scores.keys(), key=all_scores.get)
  print("Top student:", top_student, "with score", all_scores[top_student])
  print("Lowest student:", lowest_student, "with score", all_scores[lowest_student])

else:
  print("No students left in the dictionary.")
