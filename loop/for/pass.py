# Scenario: You’re planning a weekly study schedule for 5 days, but you haven’t decided what to study on some days yet.

for day in range(1, 6):  # Loop through 5 days
    if day == 3:  # Wednesday is undecided
        print(f"Day {day}: No plan yet.")
        pass  # Placeholder for future study plan
    else:
        print(f"Day {day}: Study Math.")
        
# Explanation: The pass statement acts as a placeholder for Day 3, allowing the loop to continue without errors while you plan later, like leaving a blank in a schedule.