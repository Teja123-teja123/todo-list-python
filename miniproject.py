# Simple To-Do List App (Dynamic, Interactive Input)

import os

TASKS_FILE = "todo.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                task, status = line.strip().split("|")
                tasks.append({"task": task, "done": status == "done"})
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            status = "done" if task["done"] else "not_done"
            file.write(f"{task['task']}|{status}\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, start=1):
            status = "✔" if task["done"] else "✘"
            print(f"{idx}. [{status}] {task['task']}")

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        print("Task added.")
    else:
        print("Task cannot be empty.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter the task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter the task number to mark as done: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["done"] = True
            print(f"Task marked as done: {tasks[index - 1]['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Save & Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
