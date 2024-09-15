""" 
Exercise: Conditional Statements
In this exercise, you will use conditional statements to categorise people based on their ages.
"""

# 1. Ask the user for their age as input and convert it to an integer.
user_age_str = input("Enter your age: ")
# Convert the user_age_str to an integer

# Convert the user_age_str to an integer
user_age_int = int(user_age_str)
# 2. Use conditional statements to categorise the user into one of the following categories:
# - If age is less than 18, print "You are a minor."
# - If age is between 18 and 65 (inclusive), print "You are an adult.
# - If age is 66 or higher, print "You are a senior citizen."

if user_age_int < 18:
    print("Your a minor.")
elif user_age_int >= 18 and user_age_int <= 65:
    print("Your are an adult.")
else:
    print("Your are a senior citizen.")



""" 
Exercise: Conditional Statements
In this exercise, you will use conditional statements to check if a year is a leap year.
"""

year = 0000



"""
Exercise: Loops
In this exercise, you will use a loop to print numbers up to a user-defined limit.
"""

# 1. Ask the user to enter a number as the limit and convert it to an integer.
limit_str = input("Enter a number as the limit: ")
limit_int = int(limit_str)  # Convert the limit_str to an integer

# 2. Use a  for loop to iterate from 1 to the user-defined limit (inclusive) and print each number.
for i in range(1, limit_int + 1):
    print(i)

# Use a while loop to iterate from 1 to the user-defined limit (inclusive) and print each number.
# Initialise a variable to start the loop
number = 1
while number <= limit_int:
    #print number
    print(number)
    # Increment number in each iteration
    number += 1   
    pass


"""
Exercise: Loop Control Statements
In this exercise, you will use a loop and loop control statements to print odd numbers.
"""

# 1. Ask the user to enter a number as the limit and convert it to an integer.
limit_str = input("Enter a number as the limit: ")
limit_int = int(limit_str) # Convert the limit_str to an integer

# 2. Use a for loop to iterate from 1 to the user-defined limit (inclusive).
# 3. Inside the loop, use a loop control statement to skip even numbers and print odd numbers.
# Fill in the code to achieve the goal:

for number in range(1, limit_int + 1, 2):
    # Add code to check if number is odd and print odd numbers
    print(number)
    pass


"""
Exercise: Nested Loops
In this exercise, you will use nested loops to generate a multiplication table.
"""
# 1. Ask the user for a number as the multiplier and convert it to an integer.
multiplier_str = input("Enter a number as the multiplier: ")
multiplier_int = int(multiplier_str)# Convert the multiplier_str to an integer

# 2. Use nested loops to generate a multiplication table.
# The outer loop iterates from 10 to 1.
# The inner loop iterates the user-defined multiplier to 1.
# Fill in the code to complete the nested loops:

for number_x in range(10, 1, -1):
    for number_y in range(1, multiplier_int):
        # Add code to print the multiplication table
        print(number_x ,"*", number_y, "=", number_x * number_y)
        
        pass
    pass
