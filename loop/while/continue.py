# Scenario: You’re packing snacks for a trip, but you skip any snacks that are expired.

snacks =  ["chips", "expired yogurt", "apple", "expired candy", "banana"]
index = 0
while index < len(snacks):
    if "expired" in snacks[index]:
        print(f"Skipping {snacks[index]}...")
        index += 1
        continue  # Skip expired snacks, move to next
    print(f"Packing {snacks[index]}")
    index += 1
    
# Explanation: The continue skips packing expired snacks, jumping to the next iteration, just like you’d skip bad food in real life.