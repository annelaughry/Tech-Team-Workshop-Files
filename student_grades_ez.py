#Define a list of student names
students = ["Alice", "Bob", "Charlie", "David", "Eva"]

# Define a dictionary to hold the scores of the students
scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eva": 88
}

# Calculate the average score using built-in functions
total_score = sum(scores.values())  # sum is a built-in function
num_students = len(scores)  # len is a built-in function
average_score = total_score / num_students  # division

print(f"Average Score: {average_score:.2f}")  # print and f-string formatting

# Use a for loop to print each student's name and score
for student in students:
    score = scores.get(student, 0)  # get is a built-in dictionary method
    print(f"Student: {student}, Score: {score}")

# Check if any student's score is above the average using a list comprehension
above_average_students = [student for student in students if scores.get(student, 0) > average_score]

print("Students scoring above average:")
for student in above_average_students:
    print(student)