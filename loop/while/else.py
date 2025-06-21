# Scenario: You’re waiting for a bus that comes every 10 minutes. If you wait 10 minutes without seeing the bus, you decide to walk instead.

wait_time = 0
bus_arrived = False
while wait_time < 10:
    wait_time += 1
    print(f"Waiting {wait_time} minute(s)...")
    if bus_arrived:  # Simulating bus arrival (set to False here)
        print("Bus is here!")
        break
else:
    print("No bus after 10 minutes, I’ll walk!")
    
# Explanation: The else runs when the loop completes without a break, representing walking when no bus arrives.