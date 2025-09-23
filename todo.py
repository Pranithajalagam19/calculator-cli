
# todo.py

def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter the new task: ")
    if task:
        tasks.append(task)
        print("Task added.")
    else:
        print("No task entered.")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            idx = int(input("Enter the task number to remove: ")) - 1
            if 0 <= idx < len(tasks):
                removed = tasks.pop(idx)
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nOptions: [1] View Tasks [2] Add Task [3] Remove Task [4] Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)  # ensure latest changes are saved
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()