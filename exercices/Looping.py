# Create a loop to display 'Goodbye' 5 times
for i in range(5):
    print('Goodbye')

# Create a loop from 1 to 10 
# For each iteration check if index is even or odd and. If even add to a total var. Dsplay the total at the end of the loop
total = 0
for i in range(1, 11):
    if i % 2 == 0:
     total += i
print(f'Total of even numbers is: {total}')

# Use a loop to go through sentence
# For each char, if is vowel: print uppercase, 
# If char is consonant: print lowercase, 
# If char not a letter: print '_'
text = input('Write a sentence: ')
for char in text:
    if char.lower() in 'aeiou':
        print(char.upper(), end='')
    elif char.isalpha():
        print(char.lower(), end='')
    else:
        print('_', end='')