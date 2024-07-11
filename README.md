 To-doApplication
 
The To-Do List Management System is a command-line application that allows users to manage their tasks efficiently. The system enables users to view tasks, add new tasks, mark tasks as completed, and delete tasks. The application runs in an interactive loop, allowing users to continuously manage their tasks until they choose to exit.
Function Definitions
1. show_tasks()
Description: Displays all tasks in the to-do list along with their completion status.
Parameters: None
Returns: None
Behavior:
•	If the todo_list is empty, it prints "No tasks in your to-do list."
•	Otherwise, it iterates through the todo_list and prints each task with its index and status ("Completed" or "Pending").
2. create_task(task_description)
Description: Adds a new task to the to-do list.
Parameters:
•	task_description (str): The description of the task to be added.
Returns: None
Behavior:
•	Creates a new dictionary representing the task with name set to task_description and done set to False.
•	Appends the new task dictionary to the todo_list.
•	Prints a confirmation message indicating that the task has been added.
3. complete_task(task_index)
Description: Marks a specified task as completed.
Parameters:
•	task_index (int): The 1-based index of the task to be marked as completed.
Returns: None
Behavior:
•	Checks if the task_index is valid (i.e., within the range of the todo_list).
•	If valid, sets the done status of the specified task to True and prints a confirmation message.
•	If invalid, prints an error message indicating that the task number is invalid.
4. delete_task(task_index)
Description: Deletes a specified task from the to-do list.
Parameters:
•	task_index (int): The 1-based index of the task to be deleted.
Returns: None
Behavior:
•	Checks if the task_index is valid (i.e., within the range of the todo_list).
•	If valid, removes the specified task from the todo_list and prints a confirmation message.
•	If invalid, prints an error message indicating that the task number is invalid.
Main Loop
The main loop provides an interactive interface for the user to manage tasks. The following options are available:
1.	Show tasks: Calls the show_tasks() function to display all current tasks.
2.	Add a task: Prompts the user to enter a task description and calls the create_task(task_description) function to add the task.
3.	Complete a task: Displays current tasks, prompts the user to enter the task number to mark as completed, and calls the complete_task(task_index) function with the provided index.
4.	Delete a task: Displays current tasks, prompts the user to enter the task number to delete, and calls the delete_task(task_index) function with the provided index.
5.	Exit: Exits the loop and terminates the program.

