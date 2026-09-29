# To-Do List

print("===== TO-DO LIST =====")

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")

        if task == "":
            print("Task cannot be empty.")
        else:
            tasks.append({
                "task": task,
                "completed": False
            })

            print("Task added successfully.")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")

        else:
            print("\n----- TASKS -----")

            for index, item in enumerate(tasks, start=1):
                if item["completed"]:
                    status = "Completed"
                else:
                    status = "Pending"

                print(index, ".", item["task"], "-", status)

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks found.")

        else:
            task_number = int(input("Enter task number to complete: "))

            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print("Task marked as completed.")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks found.")

        else:
            task_number = int(input("Enter task number to delete: "))

            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print("Deleted:", deleted_task["task"])
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Exiting To-Do List...")
        break

    else:
        print("Invalid choice. Please try again.")