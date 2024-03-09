 
# Function to add two numbers 
def add(num1, num2): 
	return num1 + num2 

# Function to subtract two numbers 
def subtract(num1, num2): 
	return num1 - num2 

# Function to multiply two numbers 
def multiply(num1, num2): 
	return num1 * num2 

# Function to divide two numbers 
def divide(num1, num2): 
	return num1 / num2 

print("Please select operation -1. Add 2. Subtract 3. Multiply 4. Divide\n") 


# Take input from the user 
select = input("Select operations form 1, 2, 3, 4 :") 

num1= int(input("Enter first number: ")) 
num2 = int(input("Enter second number: ")) 

if select == '1': 
	print(number_1, "+", number_2, "=", 
					add(num1, num2)) 

elif select == '2': 
	print(number_1, "-", number_2, "=", 
					subtract(num1, num2)) 

elif select == '3': 
	print(number_1, "*", number_2, "=", 
					multiply(num1, num2)) 

elif select == '4': 
	print(number_1, "/", number_2, "=", 
					divide(num1, num2)) 
else: 
	print("Invalid input") 
