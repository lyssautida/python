#Task {name: str, completed: bool}

def add_task(tasks, task_name = "default task"):
    task = {"name": task_name, "completed": False }
    tasks.append(task)
    print(f"Task {task_name} added successfully")
    return

def list_tasks(tasks):
    print("\nTASK LIST")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        task_name = task["name"]
        print(f" [{status}] {index}.{task_name}")

def update_task_name(tasks, index, new_task_name):
    task_index = int(index) - 1
    if task_index >= 0 and task_index < len(tasks):
        tasks[task_index]["name"] = new_task_name
        print(f"Task {index} updated to {new_task_name}")
    else:
        print("Invalid task index")
    return

def complete_task(tasks, index):
    task_index = int(index) - 1
    if task_index >= 0 and task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"Task {index} completed")
    else:
        print("Invalid task index")
    return

def delete_task(tasks):
    for task in tasks:
        if task["completed"]:
            tasks.remove(task)
    print("Completed tasks deleted successfully")
    return

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
    elif choice == "3":
        list_tasks(tasks)
        task_index = input("Task index: ")
        new_task_name = input("New task name: ")
        update_task_name(tasks, task_index, new_task_name)
    elif choice == "4":
        list_tasks(tasks)
        task_index = input("Task index: ")
        complete_task(tasks, task_index)
    elif choice == "5":
        list_tasks(tasks)
        delete_task(tasks)
        list_tasks(tasks)
    elif choice == "6":
        print("Bye.")
        break

    print("The end")

