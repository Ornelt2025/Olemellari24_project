import os
import json

FILENAME = "todo_list.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def main():
    tasks = load_tasks()
    
    while True:
        print("Choose an option:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Quit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task = input("Enter a new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("Task added.\n")
        elif choice == "3":
            show_tasks(tasks)
            try:
                task_num = int(input("Enter task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"Removed task: {removed}\n")
                else:
                    print("Invalid task number.\n")
            except ValueError:
                print("Please enter a valid number.\n")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
