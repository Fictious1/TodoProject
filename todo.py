tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task has been Added!")

    elif choice == '2':
        print("\nYour Tasks:")
        
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks):
                print(i + 1, task)

    elif choice == '3':
        num = int(input("Enter task number to delete: "))
        
        if num <= len(tasks):
            tasks.pop(num - 1)
            print("Task Deleted!")
        else:
            print("Invalid task number.")

    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid option.")