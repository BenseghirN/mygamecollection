# Ask the user for 10 numbers and put them in a list. Find the max abd sum all the elements in the list.

numbers = [int(input(f"Enter number #{i+1}: ")) for i in range(10)]
max_number = max(numbers)
total_sum = sum(numbers)
print(f"The maximum number is: {max_number}")
print(f"The sum of all numbers is: {total_sum}")