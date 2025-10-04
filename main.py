tasks = []

while True:
    print("1.Add Task")
    print("2.Remove Task")
    print("3.Show Task")
    print("4.Quit")
    choice = input("Please Enter Your Choice: ")

    if choice.startswith("1"):
        task = input("Enter a task: ")
        tasks.append(task)
    elif choice.startswith("2"):
        task = input("Enter a task: ")
        if task in tasks:
            tasks.remove(task)
        else:
            print("Its not in tasks list.")
    elif choice.startswith("3"):
        print(tasks)
    elif choice.startswith("4"):
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice.")



