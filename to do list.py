class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

def add_task(task_list):
    description = input("Enter the task description: ")
    task = Task(description)
    task_list.append(task)
    print(f"Task '{description}' added.")

def view_tasks(task_list):
    if not task_list:
        print("No tasks in the list.")
        return

    print("Tasks:")
    for index, task in enumerate(task_list):
        status = "Done" if task.completed else "Pending"
        print(f"{index + 1}. {task.description} - {status}")

def remove_task(task_list):
    view_tasks(task_list)
    try:
        task_number = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_number < len(task_list):
            removed_task = task_list.pop(task_number)
            print(f"Task '{removed_task.description}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def mark_task_as_completed(task_list):
    view_tasks(task_list)
    try:
        task_number = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_number < len(task_list):
            task_list[task_number].mark_as_completed()
            print(f"Task '{task_list[task_number].description}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    task_list = []
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task(task_list)
        elif choice == '2':
            view_tasks(task_list)
        elif choice == '3':
            remove_task(task_list)
        elif choice == '4':
            mark_task_as_completed(task_list)
        elif choice == '5':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
