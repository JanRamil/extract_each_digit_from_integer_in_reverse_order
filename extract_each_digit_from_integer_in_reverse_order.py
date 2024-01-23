 # Write a Program to extract each digit from an integer in the reverse order
 # Exercise 11
 
 # Create pseudocode
 
 # Create a code that will ask to input a number
number = int(input("Please enter a number here: "))

# Create a code that will print the number that you entered
print("You entered: ", number)

# Create a code that will reverse the number
while number > 0:
    # Create a code that will extract the last digit
    reversed_number = number % 10
    # Create a code that will remove the last digit
    number = number // 10 
    
    # Create a code that will print the number in reversed manner
    print(reversed_number, end=" ")
    
        
    
 
 