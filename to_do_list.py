task_list = []
completed_list = []

def add_task():
    task = input("\nEnter the task you would like to add: ")
    if task.isnumeric():
        print("Task name must be a string.\n")
        return
    elif task in task_list:
        print("Task already exists in the list.\n")
    #end if
    
    task_list.append(task)
    completed_list.append("Incomplete")
    print(f"{task} successfully added to the list.\n")
    return task_list, completed_list
#end function

def view_tasks():
    if len(task_list) == 0:
        print("\nThe list is empty.\n")
        return
    print("\nTo-do list:")
    for index in range(len(task_list)):
        print(f"{index + 1}. {task_list[index]} ({completed_list[index]})")
    #end for
    print()
#end function

def mark_complete():
    if len(task_list) == 0:
        print("\nThere are no items to mark complete.\n")
        return
    task = input("\nEnter the task you would like to mark as complete: ")
    if task not in task_list:
        print("Task not found in the list.\n")
        return
    else:
        index = task_list.index(task)
        completed_list[index] = "Complete"
        print(f"{task} has been marked as complete.\n")
    #end if
#end function

def delete_task():
    if len(task_list) == 0:
        print("\nThere are no items to delete.\n")
        return
    task = input("\nEnter the task you would like to delete: ")
    if task not in task_list:
        print("Task not found in the list.\n")
        return
    else:
        index = task_list.index(task)
        task_list.pop(index)
        completed_list.pop(index)
        print(f"{task} has been deleted from the list.\n")
    #end if
#end function

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
        print("\nInvalid input. Please enter a number.\n")
        continue
    except Exception as e:
        print("\nAn error occurred. Please try again.\n")
        continue
    else:
        if choice < 1 or choice > 5:
            print("\nInvalid choice. Please enter a number between 1 and 5.\n")
            continue
        elif choice == 1:
            add_task()
        elif choice == 2:
            delete_task()
        elif choice == 3:
            mark_complete()
        elif choice == 4:
            view_tasks()
        elif choice == 5:
            break
        #end if
    #end try-except
#end while
print("\nThank you for using the To-Do List App!")