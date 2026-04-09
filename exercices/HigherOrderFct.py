# Create a lambda fct that return the sum of 3 numbers and store it in a var. Display result
sum = lambda x, y, z: x + y + z
print(sum(10, 20, 30))

# Create a lambda fct and use it in a map to convert each Celsius temp to Fahrenheit
# Show the stored result in a list
temps = [10, 20, 22, 25]
convert_to_fahrenheit = lambda x: x * 9 / 5 + 32
print(list(map(convert_to_fahrenheit, temps)))