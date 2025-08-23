# You are given two arrays a[] and b[], return the Union of both the arrays in any order.
# គេប្រគល់ឪ្យអ្នកនូវ lists(arrays) ចំនូនពីរគឺ a[] នឹង b[], សូមរក list(array) នៃចំនួនប្រជុំរបស់ list(array) ទាំងពីរ។

# The Union of two arrays is a collection of all distinct elements present in either of the arrays. If an element appears more than once in one or both arrays, it should be included only once in the result.
# list ប្រជុំនៃ arrays ទាំងពិរគឺជាបណ្ដុំនៃ arrays ទាំងពិរដែលមិនមានចំនួនដដែលនៅក្នុងនោះ។ ប្រសិនជាមានធាតុដូចគ្នាដែលមាននៅក្នុង arrays ទាំងពីរ នោះវាគួរតែរាប់បញ្ចូលក្នុង arrays ថ្មីចំនួនមួយដងប៉ុណ្ណោះ។

# Note: Elements of a[] and b[] are not necessarily distinct.
# ចំណាំ: ធាតុទាំងអស់នៅក្នុង​ a[] និង b[] មិនប្រាកដថាមិនមានធាតុជាន់គ្នានោះទេ។ 
# Note that, You can return the Union in any order but the driver code will print the result in sorted order only.
# ចំណាំ, អ្នកអាច return មកវិញនូវ array នៃធាតុប្រជុំនៅក្នុង array ដែលមិនបានរៀបរៀង(sorted), តែកូដ(code)ដែល print ចេញមកត្រូវតែតាមលំដាប់លំដោយ។ 

# Example 1:
# Input: a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
# Output: [1, 2, 3]
# Explanation: Union set of both the arrays will be 1, 2 and 3.


# Example 2:
# Input: a[] = [1, 2, 3], b[] = [4, 5, 6] 
# Output: [1, 2, 3, 4, 5, 6]
# Explanation: Union set of both the arrays will be 1, 2, 3, 4, 5 and 6.


# Example 3:
# Input: a[] = [1, 2, 1, 1, 2], b[] = [2, 2, 1, 2, 1] 
# Output: [1, 2]
# Explanation: Union set of both the arrays will be 1 and 2.

# Guide:
# - Create a function(union):
#   - It returns the union array value of 2 input array
#     - 1st parameter: first_array: for the a[]
#     - 2nd parameter: second_array: for the b[]
# - Create another function(sort) that take 2 parameters:
#   - It returns the sorted versions of the input array by the input direction
#     - 1st parameter: array: for the array[]
#     - 2nd parameter: direction: either desc or asc
# - Printing out the result by using the combination of sort and union function 


# Hint: Please reviews the lessons below to solve this problem
# - Data type: List(array)
#   - List.append(element): append element to the list
#     - E.g. 
#       a = [1, 2, 3]
#       a.append(4) # a = [1, 2, 3, 4]
#   - List.remove(element): remove element from the list
#     - E.g.
#       b = [1, 2, 3] 
#       a.remove(2) # a = [1, 3]
#   - 
# - Loop: for and while
# - Function