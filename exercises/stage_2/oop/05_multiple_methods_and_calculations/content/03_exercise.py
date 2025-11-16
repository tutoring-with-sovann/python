# Exercise 3: Complex Methods with Multiple Operations (Hard)
# Description: Create a Fraction class that performs comprehensive fraction arithmetic
#
# Tasks:
# 1. Create a Fraction class with __init__ constructor
# 2. Constructor should accept: numerator, denominator
# 3. Create these methods:
#    - simplify() - simplifies the fraction (divide both by GCD)
#    - to_decimal() - returns decimal value
#    - add(other_fraction) - adds another fraction and returns new simplified Fraction
#    - subtract(other_fraction) - subtracts another fraction and returns new simplified Fraction
#    - multiply(other_fraction) - multiplies by another fraction and returns new simplified Fraction
#    - divide(other_fraction) - divides by another fraction and returns new simplified Fraction
#    - is_greater_than(other_fraction) - returns True if this fraction is greater
#    - is_equal_to(other_fraction) - returns True if fractions are equal (compare cross products)
#    - get_reciprocal() - returns new Fraction that is reciprocal (swap num/den)
# 4. Create multiple fractions and test all operations including comparisons
#
# Expected Output:
# Fraction: 6/8
# After simplifying: 3/4
# As decimal: 0.75
# 3/4 + 1/2 = 5/4
# 3/4 - 1/2 = 1/4
# 3/4 * 2/3 = 1/2
# 3/4 / 1/2 = 3/2
# Is 3/4 > 1/2? True
# Is 3/4 equal to 6/8? True
# Reciprocal of 3/4 is 4/3
#
# Hint:
# - Addition: a/b + c/d = (a*d + b*c)/(b*d)
# - Subtraction: a/b - c/d = (a*d - b*c)/(b*d)
# - Multiplication: a/b * c/d = (a*c)/(b*d)
# - Division: a/b / c/d = (a*d)/(b*c)
# - Comparison: a/b > c/d if a*d > b*c

# Write your code here:
