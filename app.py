import os

# Constants
TASKS_FILE = "tasks.txt"

def display_menu():
    print("Terminal Todo App\n")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit\n")

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

tasks = load_tasks()

def view_tasks():
    if not tasks:
        print("No tasks yet!\n")
    else:
        print("Your Tasks:\n")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
        print()

def add_task():
    new_task = input("Enter a new task: ")
    tasks.append(new_task)
    save_tasks()
    print("Task added!\n")

def delete_task():
    view_tasks()
    task_index = int(input("Enter the task number to delete: ")) - 1
    
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        save_tasks()
        print(f"Task '{deleted_task}' deleted.\n")
    else:
        print("Invalid task number.\n")

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting. Have a great day!")
            break
        else:
            print("Invalid choice. Please select again.\n")

if __name__ == "__main__":
    main()
