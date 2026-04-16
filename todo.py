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