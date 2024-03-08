# Function to display the to-do list
def display_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("Your to-do list:")
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task}")

# Function to add a task to the to-do list
def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to your to-do list.")

# Function to remove a task from the to-do list
def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from your to-do list.")
    else:
        print("Invalid task index!")

def main():
    todo_list = []

    while True:
        print("\nWhat would you like to do?")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_list(todo_list)
        elif choice == "2":
            task = input("Enter the task you want to add: ")
            add_task(todo_list, task)
        elif choice == "3":
            task_index =int(input("Enter the index of the task you want to remove: "))
            remove_task(todo_list, task_index)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__== "__main__":
    main()