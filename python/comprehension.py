"""
List comprehension is mainly done for data processing, but in some cases it may be useful for other kinds of tasks.
"""

numbers = [1,2,3]
double_numbers = [x * 2 for x in numbers]
print(double_numbers)

# matrix case 
list_of_numbers = [[1,2,3],[1,2,3],[1,2,3]]
double_list_of_numbers = [num * 2 for num_list in list_of_numbers for num in num_list]
print(double_list_of_numbers)

