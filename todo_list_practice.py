def display_menu():
    print("1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Calculate total time")
    print("5. Quit")

def add_item(todo_list):
    name = input("Enter task: ")
    time = float(input("Enter minutes to complete: "))
    item = {'name': name, 'minutes': time}
    todo_list.append(item)
    print(f"{name} has been added to the list.")

def view_list(todo_list):
    if not todo_list:
        print("Your To-Do list is empty.")
    else:
        for item in todo_list:
            print(f"Task: {item['name']}, Minutes: {item['minutes']}")

def remove_item(todo_list):
    name = input("Enter the name of the task to remove: ")
    for item in todo_list:
        if item['name'] == name:
            todo_list.remove(item)
            print(f"{name} has been removed from the list.")
            break
    else:
        print(f"{name} is not in the To-Do list.")

def calculate_total_time(todo_list):
    total_time = 0
    for item in todo_list:
        total_time += item['minutes']
    print(f"Total time to complete your To-Do list: 1{total_time:.2f} minutes")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_item(todo_list)
        elif choice == '2':
            view_list(todo_list)
        elif choice == '3':
            remove_item(todo_list)
        elif choice == '4':
            calculate_total_time(todo_list)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()