def add_task(task_list, completed_list):
    task = input("Enter the task you would like to add: ")
    if task.isnumeric():
        print("Task name must be a string.\n")
        return
    elif task in task_list:
        print("Task already exists in the list.\n")
    #end if
    
    task_list.append(task)
    completed_list.append(False)
    return task_list, completed_list
#end function

def view_tasks():
    pass
#end function

def mark_complete():
    pass
#end function

def delete_task():
    pass
#end function

task_list = []
completed_list = []

while True:
    print("Welcome to the To-Do List App!\n\nMenu:")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. Mark a task as complete")
    print("4. View tasks")
    print("5. Exit")
    
    try:
        choice = int(input("Please enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        continue
    except Exception as e:
        print("An error occurred. Please try again.\n")
        continue
    else:
        if choice < 1 or choice > 5:
            print("Invalid choice. Please enter a number between 1 and 5.\n")
            continue
        elif choice == 1:
            task_list, completed_list = add_task(task_list, completed_list)
        elif choice == 2:
            delete_task()
        elif choice == 3:
            mark_complete()
        elif choice == 4:
            view_tasks
        elif choice == 5:
            break
    #end try-except
    
    #end if
#end while