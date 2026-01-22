#Task {name: str, completed: bool}

def add_task(tasks, task_name = "default task"):
    task = {"name": task_name, "completed": False }
    tasks.append(task)
    print(f"Task {task_name} added successfully")
    return

def list_tasks(tasks):
    print("\nTask List")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        task_name = task["name"]
        print(f"{index}. [{status}] {task_name}")

tasks = []
while True:
    print("\nMenu task manager")
    print("1. Add")
    print("2. List")
    print("3. Edit")
    print("4. Complete")
    print("5. Delete")
    print("6. End")

    choice = input("Type your choice ")

    if choice == "1":
        task_name = input("Write the task name you're about to create: ")
        add_task(tasks, task_name)
    elif choice == "2":
        list_tasks(tasks)
    elif choice == "6":
        print("Bye.")
        break

    print("The end")

