# Scenario: You’re counting how many push-ups you can do each day, starting from 5 and increasing by 2 each day for a week.

for count in range(5, 12, 2):  # Start at 5, stop before 12, step by 2
    print(f"Day {count//2}: Do {count} push-ups.")
    
# Explanation: The range(5, 12, 2) generates numbers (5, 7, 9, 11), representing push-up counts, showing how range() creates a sequence to control loop iterations, like planning exercise goals.