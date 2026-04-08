# Create a program that ask the user for 2 numbers
# If one is positive and the other is negative, print "Congratulations!" 
# print("Enter the first number:")
# num1 = float(input())
# print("Enter the second number:")
# num2 = float(input())

num1, num2 = map(float, input("Enter two numbers separated by space: ").split())

match (num1, num2):
    case (x, y) if (x > 0 and y < 0) or (x < 0 and y > 0):  
        print("Congratulations!")
    case _:
        print("Try again!") 


        




