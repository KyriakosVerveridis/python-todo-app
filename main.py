import functions

# tasks = []

while True:
    print("1.Add Task")
    print("2.Remove Task")
    print("3.Show Tasks")
    print("4.Quit")
    choice = input("Please Enter Your Choice: ")

    if choice.startswith("1"):
        task = input("Enter a task: ")
        tasks = functions.get_tasks()
        tasks.append(task + "\n")
        functions.write_tasks(tasks,"tasks.txt")
    elif choice.startswith("2"):
        tasks = functions.get_tasks()
        task = input("Enter a task: ") + "\n"

        if task in tasks:
            tasks.remove(task)
            functions.write_tasks(tasks, "tasks.txt")
        else:
            print("Its not in tasks list.")
    elif choice.startswith("3"):
        for item in tasks:
            item = item.strip("\n")
            print(item)
    elif choice.startswith("4"):
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice.")



