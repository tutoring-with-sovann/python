# Exercise 3: Multiple Methods with State Changes (Hard)
# Description: Create a TimerClass that tracks time and can pause/resume
#
# Tasks:
# 1. Create a Timer class with __init__ constructor
# 2. Constructor should initialize: seconds (0), is_running (False)
# 3. Create start() method that sets is_running to True
# 4. Create stop() method that sets is_running to False
# 5. Create add_seconds(amount) method that adds seconds only if timer is running
# 6. Create reset() method that sets seconds to 0 and stops the timer
# 7. Create get_time_display() method that returns time as "MM:SS" format
# 8. Create a timer and test all functionality
#
# Expected Output:
# Timer: 00:00, Running: False
# Starting timer...
# Adding 75 seconds...
# Timer: 01:15, Running: True
# Adding 30 seconds while stopped...
# Timer: 01:15, Running: False
# Resetting...
# Timer: 00:00, Running: False
#
# Hint: Use // for integer division and % for remainder to format time

# Write your code here:
