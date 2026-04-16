# To-Do List Application
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

# Test
add_task("Buy groceries")
add_task("Complete homework")
print(f"Total Tasks: {len(tasks)}")