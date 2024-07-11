# Initialize an empty list for tasks
todo_list = []

# Function to display the tasks
def show_tasks():
    if not todo_list:
        print("No tasks in your to-do list.")
    else:
        print("Tasks in your To-Do List:")
        for index, item in enumerate(todo_list, start=1):
            status = "Completed" if item["done"] else "Pending"
            print(f"{index}. {item['name']} - {status}")

# Function to add a task
def create_task(task_description):
    task = {"name": task_description, "done": False}
    todo_list.append(task)
    print(f"Task '{task_description}' has been added.")

# Function to mark a task as done
def complete_task(task_index):
    if 1 <= task_index <= len(todo_list):
        todo_list[task_index - 1]["done"] = True
        print(f"Task {task_index} marked as done.")
    else:
        print("Invalid task number. Please choose a valid task number.")

# Function to delete a task
def delete_task(task_index):
    if 1 <= task_index <= len(todo_list):
        removed = todo_list.pop(task_index - 1)
        print(f"Task '{removed['name']}' has been removed.")
    else:
        print("Invalid task number. Please choose a valid task number.")

# Main loop to handle user inputs
while True:
    print("\nOptions:")
    print("1. Show tasks")
    print("2. Add a task")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task_description = input("Enter the task description: ")
        create_task(task_description)
    elif choice == '3':
        show_tasks()
        task_index = int(input("Enter the task number to mark as done: "))
        complete_task(task_index)
    elif choice == '4':
        show_tasks()
        task_index = int(input("Enter the task number to delete: "))
        delete_task(task_index)
    elif choice == '5':
        break
    else:
        print("Invalid option. Please select a valid choice.")
