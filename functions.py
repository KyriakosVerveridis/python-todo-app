def get_tasks(filepath="tasks.txt"):
    with open(filepath,"r")as file:
        tasks_file = file.readlines()
        return tasks_file

def write_tasks(tasks,filepath="tasks.txt"):
    with open(filepath,"w")as file:
        file.writelines(tasks)