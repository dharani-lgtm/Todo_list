# To-Do List Application
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

# Test
add_task("Buy groceries")
add_task("Complete homework")
print(f"Total Tasks: {len(tasks)}")

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task deleted: {task}")
    else:
        print(f"Task not found: {task}")

# Test
delete_task("Buy groceries")
print(f"Total Tasks: {len(tasks)}")
=======


def view_tasks():
    if len(tasks) == 0:
        print("No tasks found!")
    else:
        print("\nAll Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Test
view_tasks()