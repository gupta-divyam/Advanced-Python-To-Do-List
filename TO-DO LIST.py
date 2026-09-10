import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except:
            return []
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def show_menu():
    print("\n" + "=" * 35)
    print("TO-DO LIST")
    print("=" * 35)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Complete Task")
    print("6. Reset Tasks")
    print("7. Exit")
    print("=" * 35)


def add_task(tasks):
    task = input("Enter task: ").strip()

    if task == "":
        print("Task cannot be empty.")
        return

    tasks.append({
        "task": task,
        "completed": False
    })

    save_tasks(tasks)
    print("Task added.")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks found.")
        return

    print("\nYour Tasks:")
    for i in range(len(tasks)):
        if tasks[i]["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(str(i + 1) + ". " + tasks[i]["task"] + " - " + status)


def edit_task(tasks):
    if not tasks:
        print("\nNo tasks to edit.")
        return

    view_tasks(tasks)

    try:
        number = int(input("Enter task number: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        new_task = input("Enter new task: ").strip()

        if new_task == "":
            print("Task cannot be empty.")
            return

        tasks[number - 1]["task"] = new_task
        save_tasks(tasks)
        print("Task updated.")

    except ValueError:
        print("Please enter a number.")


def delete_task(tasks):
    if not tasks:
        print("\nNo tasks to delete.")
        return

    view_tasks(tasks)

    try:
        number = int(input("Enter task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        deleted = tasks.pop(number - 1)
        save_tasks(tasks)

        print("Deleted:", deleted["task"])

    except ValueError:
        print("Please enter a number.")


def complete_task(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks(tasks)

    try:
        number = int(input("Enter task number to complete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        tasks[number - 1]["completed"] = True
        save_tasks(tasks)

        print("Task completed.")

    except ValueError:
        print("Please enter a number.")


def reset_tasks(tasks):
    if not tasks:
        print("\nNo tasks to reset.")
        return

    answer = input("Delete all tasks? (yes/no): ").strip().lower()

    if answer == "yes":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks deleted.")
    else:
        print("Reset cancelled.")


def main():
    tasks = load_tasks()

    print("\nWelcome to the To-Do List!")

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            edit_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            complete_task(tasks)

        elif choice == "6":
            reset_tasks(tasks)

        elif choice == "7":
            save_tasks(tasks)
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
