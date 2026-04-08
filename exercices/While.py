# Create a game where the computer chooses a random number between 1 and 100, and the user has to guess it
# He has 10 attempts to guess the number
# After each attempt, the computer will tell him if the number is higher, lower, or correct
import random

number = random.randint(1, 100)
attempts = 10

while attempts > 0:
    guess = int(input("Guess the number between 1 and 100: "))
    if guess < number:
        print("Number is higher!")
    elif guess > number:
        print("Number is lower!")
    else:
        print("Correct! Well played")
        break
    attempts -= 1
    print(f"You have {attempts} attempts left.")
else:
    print(f"Game over! The number was {number}.")

# Use a loop to ask user for a color and display it
# Then ask if user want to continue or not
while True:
    color = input("Enter a color: ")
    print(f"You entered: {color}")
    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != "y":
        print("Goodbye!")
        break

# ctx = True
# while ctx:
#     color = input("Give a random color: ")
#     print(f"You have given the color {color}.")
#     continue_game = input("Do you want to play again? (y/n): ")
#     if continue_game == "y":
#         continue
#     else:        
#         ctx = False
#         print("Thanks for playing!")
#         break

# Use a loop to go through each char in text
# If char is not a letter skip it and continue, otherwise print it uppercase
text = input("Enter a text: ")

for char in text:
    if not char.isalpha():
        continue
    print(char.upper())
