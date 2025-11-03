import os

task_file = "./tasks.txt"


def load_tasks():
    tasks = []
    if os.path.exists(task_file):
        with open(task_file, "r", encoding="utf-8") as f:
            for line in f:
                text, status = line.strip().rsplit("||", 1)
                tasks.append({"text": text, "done": status == "done"})
    return tasks


def save_tasks(tasks):
    with open(task_file, "w") as f:
        for task in tasks:
            status = "done" if task["done"] else "not_done"
            f.write(f"{task['text']} || {status}\n")


def display_tasks(tasks):
    if not tasks:
        print("No task is Listed@")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "*" if task["done"] else " "
            print(f"{i}: [{status}] {task['text']}")


def task_manager():
    tasks = load_tasks()

    while True:
        print("\n------ Task Managener ------")
        print("1: Add Tasks")
        print("2: View Tasks")
        print("3: mark as done")
        print("4: Delete Task")
        print("5: EXIT")

        choice = input("\nEnter your choice: ").strip()

        match choice:
            case "1":
                task = input("Enter new Task: ").strip()
                if task:
                    tasks.append({"text": task, "done": False})
                    save_tasks(tasks)
                else:
                    print("Tasks can't be Empty!!")
            case "2":
                display_tasks(tasks)
            case "4":
                display_tasks(tasks)
                try:
                    index = int(input("Enter task number to delete: "))
                    if 1 <= index <= len(tasks):
                        del tasks[index - 1]
                        save_tasks(tasks)
                    else:
                        print("Task isn't avaliable..")
                except ValueError:
                    print("Invalid Input!!")
            case "3":
                display_tasks(tasks)
                try:
                    idx = int(input("Enter completed task number: "))
                    if 1 <= idx <= len(tasks):
                        tasks[idx - 1]["done"] = True
                        save_tasks(tasks)
                    else:
                        print("Invalid task Number...")
                except ValueError:
                    print("Invalid User Input!!")

            case "5":
                print("Bye! Have a good day!!")
                break
            case _:
                print("Choose valid options(1 to 5) \n           @ Try Again @")


task_manager()
