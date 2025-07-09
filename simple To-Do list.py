tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Choose (1-4): ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == '2':
        if not tasks:
            print("No tasks!")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == '3':
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        try:
            num = int(input("Task number to remove: "))
            if 1 <= num <= len(tasks):
                print(f"Removed: {tasks.pop(num - 1)}")
            else:
                print("Invalid number!")
        except:
            print("Enter a valid number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
