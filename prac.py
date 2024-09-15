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

