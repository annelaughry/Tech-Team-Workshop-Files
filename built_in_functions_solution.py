# Task 1: String Manipulation
s = "Hello, world! Welcome to the world of programming."
s_upper = s.upper()
s_replaced = s.replace("world", "Python")
print(s_upper)       # "HELLO, WORLD! WELCOME TO THE WORLD OF PROGRAMMING."
print(s_replaced)    # "Hello, Python! Welcome to the Python of programming."

# Task 2: Arithmetic Operations
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_value = max(numbers)
min_value = min(numbers)
sum_values = sum(numbers)
print(max_value)     # 9
print(min_value)     # 1
print(sum_values)    # 39

# Task 3: List Handling
sorted_numbers = sorted(numbers)
squares = [x**2 for x in numbers]
print(sorted_numbers) # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
print(squares)        # [9, 1, 16, 1, 25, 81, 4, 36, 25, 9, 25]

# Task 4: Type Conversion
num_str = "12345"
num = 6789
num_int = int(num_str)
num_str_converted = str(num)
print(num_int)           # 12345
print(num_str_converted) # "6789"

# Task 5: Input and Output
name = input("Enter your name: ")
print(f"Hello, {name}!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum_numbers = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_numbers}.")
