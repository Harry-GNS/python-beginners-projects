tasks=[]

while True:

    print("-----------------------------")
    print ("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task✅")
    print("4. Delete a task")
    print("5. Exit")

    choice=input("Enter a choice: ")

    if choice=="1":
        add_task=input("Enter the task: ")
        tasks.append(add_task)
        print("Your task has been added successfully!")

    elif choice=="2":
        if tasks!=0:
            for i, task in enumerate(tasks,1):
                print(f"{i:<1}:{task}")

        else:
            print("No task is added") 

    elif choice=="3":
        done_task=input("Enter which task would you like to ✅: ")
        task_number=int(done_task) - 1
        
        if 0<=task_number<=len(tasks):
            tasks[task_number]= tasks[task_number] + "✅"
            print("Task marked as ✅")

        else:
            print("Invalid option")


    elif choice=="4":
        delete_task=input("Enter which task would you like to delete: ") 
        deleted_task=int(delete_task)-1
        del tasks[deleted_task]  
        print("task deleted successfully!")

    elif choice=="5":
        print("system close")
        break             
                    









