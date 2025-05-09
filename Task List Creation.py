import os #Import the OS module to be able to check if the file (task.txt) exists

FILENAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return [] #It will return an empty output if the file does not exist
    with open(FILENAME, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as file: #The 'w' means the file is opened in write mode
        for task in tasks:
            file.write(task + "\n") #This will create a loop through the list and write each new task to a new line

def show_tasks(tasks):
    if not tasks:
        print("There are no tasks. :(")
    else:
        print("Task List:")
        for i, task in enumerate(tasks, 1): #enumerate means it will begin from the first task using the numbers placed on each task (index numbers)
            print(f"{i}. {task}")

def add_task(tasks):
    new_task = input("Add new task: ").strip()
    if new_task:
        tasks.append(new_task)
        save_tasks(tasks)
        print("Task has been added.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Type the task number you wish to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"The task '{removed}' has been removed.")
        else:
            print("Invalid Number.")
    except ValueError:
        print("Numbers, not letters.")

def main():
    tasks = load_tasks()
    while True:
        print("\nMenu:")
        print("1. Task Creation")
        print("2. Task Deletion")
        print("3. Task Viewing")
        print("4. Exit")

        choice = input("Pick a selection (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            delete_task(tasks)
        elif choice == "3":
            show_tasks(tasks)
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
