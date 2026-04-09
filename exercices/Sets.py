# 1. Find common elements
# Write a function common_elements(list1, list2) that takes two lists as input
# and returns a list containing only the elements present in both lists, without duplicates.
# output : common_elements([1, 2, 3, 4], [3, 4, 5, 6]) => [3, 4]
def common_elements(list1, list2):
    common = set(list1) & set(list2)
    return list(common)

print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))

# 2. Remove duplicates
# Write a function remove_duplicates(lst) that takes a list as input
# and returns a new list containing the same elements, but without duplicates.
# output : remove_duplicates([1, 2, 2, 3, 4, 4, 5]) => [1, 2, 3, 4, 5]

def remove_duplicate(lst):
    return list(set(lst))

print(remove_duplicate([1, 2, 2, 3, 4, 4, 5]))

# 3. Find unique elements
# Write a function unique_elements(list1, list2) that takes two lists as input
# and returns a list containing the elements that appear in only one of the two lists,
# without duplicates.
# output : unique_elements([1, 2, 3], [2, 3, 4]) => [1, 4]

def unique_elements(list1, list2):
    unique = set(list1) ^ set(list2)
    return list(unique)

print(unique_elements([1, 2, 3], [2, 3, 4]))

# 4. Check for common elements
# Write a function has_common_elements(list1, list2) that takes two lists as input
# and returns True if they have at least one element in common, otherwise False.
# outputs :
# has_common_elements([1, 2, 3], [4, 5, 6]) => False
# has_common_elements([1, 2, 3], [3, 4, 5]) => True

def has_common_elements(list1, list2):
    return bool(set(list1) & set(list2))

print(has_common_elements([1, 2, 3], [4, 5, 6]))
print(has_common_elements([1, 2, 3], [3, 4, 5]))

# 5. Count unique elements
# Write a function count_unique_elements(lst) that takes a list as input
# and returns the number of unique elements it contains.
# output : count_unique_elements([1, 2, 2, 3, 3, 3, 4]) => 4

def count_unique_elements(lst):
    return len(set(lst))

print(count_unique_elements([1, 2, 2, 3, 3, 3, 4]))