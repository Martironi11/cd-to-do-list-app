def main():
    from tasks import TaskManager
    import sys

    task_manager = TaskManager()

    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task_manager.add_task(description, due_date)
            print("Task added successfully.")

        elif choice == '2':
            task_id = input("Enter task ID to remove: ")
            if task_manager.remove_task(task_id):
                print("Task removed successfully.")
            else:
                print("Task not found.")

        elif choice == '3':
            tasks = task_manager.list_tasks()
            if tasks:
                print("\nTasks:")
                for task in tasks:
                    print(task)
            else:
                print("No tasks available.")

        elif choice == '4':
            print("Exiting the application.")
            sys.exit()

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()