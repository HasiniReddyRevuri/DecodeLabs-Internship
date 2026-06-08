my_tasks = []

def show_menu():
    
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    
    task_desc = input("Enter task description: ").strip()
    if not task_desc:
        print("Error: Task description cannot be empty.")
        return
    
  
    task_row = {
        "task": task_desc,
        "done": False
    }
    my_tasks.append(task_row)
    print(f"Success: Task '{task_desc}' added!")

def view_task():
    
    if not my_tasks:
        print("No tasks yet! Your to-do list is empty.")
        return
        
    print("\nYour Tasks:")
    
    for index, task in enumerate(my_tasks, start=1):
      
        status = "✓ Done" if task["done"] else "Pending"
        print(f"[{index}] {task['task']} — [{status}]")

def mark_done():
   
    view_task()
    if not my_tasks:
        return
        
    try:
        index = int(input("Enter task number to mark done: ")) - 1
        if 0 <= index < len(my_tasks):
            my_tasks[index]["done"] = True
            print("Success: Marked as done!")
        else:
            print("Error: Invalid task selection number.")
    except ValueError: 
        print("Error: Input must be a valid numerical integer.")

def delete_task():
    view_task()
    if not my_tasks:
        return
        
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(my_tasks):
            removed = my_tasks.pop(index)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Error: Invalid task selection number.")
    except ValueError:
        print("Error: Input must be a valid numerical integer.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting backend engine. Goodbye!")
            break
        else:
            print("Invalid choice. Please pick an option from 1 to 5.")

if __name__ == "__main__":
    main()