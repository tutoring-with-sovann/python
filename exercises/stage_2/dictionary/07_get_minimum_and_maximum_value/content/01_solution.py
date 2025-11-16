scores = {
  "Alice": 85,
  "Bob": 92,
  "Charlie": 78,
  "Dara": 88
}

print("All student scores:", scores)

top_student = max(scores.keys(), key=scores.get)
lowest_student = min(scores.keys(), key=scores.get)

print("Top student:", top_student, "with score", scores[top_student])
print("Lowest student:", lowest_student, "with score", scores[lowest_student])
