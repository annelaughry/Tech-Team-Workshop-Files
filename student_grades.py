# Define a list of student names
students = ["Alice", "Bob", "Charlie", "David", "Eva"]

# Define a dictionary to hold the scores of the students
scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eva": 88
}

# Function to calculate and print the average score
def print_average_score():
    total_score = sum(scores.values())  # sum is a built-in function
    num_students = len(scores)  # len is a built-in function
    average_score = total_score / num_students  # division
    print(f"Average Score: {average_score:.2f}")  # print and f-string formatting
    return average_score

# Function to print all students' scores
def print_all_scores():
    for student in students:
        score = scores.get(student, 0)  # get is a built-in dictionary method
        print(f"Student: {student}, Score: {score}")

# Function to print students scoring above average
def print_above_average_students(average_score):
    above_average_students = [student for student in students if scores.get(student, 0) > average_score]
    print("Students scoring above average:")
    for student in above_average_students:
        print(student)

# Main loop
while True:
    print("\nOptions:")
    print("1. Print all student scores")
    print("2. Print average score")
    print("3. Print students scoring above average")
    print("4. Add or update student score")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print_all_scores()
    elif choice == '2':
        avg_score = print_average_score()
    elif choice == '3':
        avg_score = print_average_score()  # Ensure average score is up-to-date
        print_above_average_students(avg_score)
    elif choice == '4':
        student_name = input("Enter student name: ")
        student_score = int(input("Enter student score: "))
        scores[student_name] = student_score
        if student_name not in students:
            students.append(student_name)
        print(f"Score updated for {student_name}.")
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")