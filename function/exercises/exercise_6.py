# Exercise 6: Find Maximum Subarray Sum
# Problem Description:
# Create a function that finds the maximum sum of a contiguous subarray within a list of integers.
# The list may contain positive and negative numbers.
# The function should:
# 1. Iterate through the list to find all possible contiguous subarrays.
# 2. Keep track of the maximum sum found.
# 3. If the list is empty, return 0.
# 4. If all sums are negative, return the largest negative sum.
# This is an implementation of Kadane's algorithm in an imperative style.
# Example: For [1, -2, 3, -1, 2], return 4 (subarray [3, -1, 2]).
# Example: For [-2, -3, -1], return -1 (subarray [-1]).
# Example: For [], return 0.