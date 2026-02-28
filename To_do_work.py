def todo_list_app():
    # Initialize an empty list to store tasks
    tasks = []
    print("Welcome to the To-Do List Application!")

    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Remove a task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the new task: ")
            tasks.append(task)
            print(f"Task '{task}' added.")
        elif choice == '2':
            if not tasks:
                print("There are no tasks in the list.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks):
                    # Display tasks with 1-based indexing for user readability
                    print(f"{index + 1}. {task}")
        elif choice == '3':
            if not tasks:
                print("There are no tasks to remove.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task}")
                try:
                    task_num = int(input("Enter the number of the task to remove: "))
                    # Adjust from 1-based index (user input) to 0-based index (list)
                    if 0 < task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        print(f"Task '{removed_task}' removed.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    # Handle non-integer input
                    print("Invalid input. Please enter a number.")
        elif choice == '4':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    todo_list_app()
