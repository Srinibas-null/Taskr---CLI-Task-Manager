import sys
from rich.console import Console
from rich.table import Table
import json

console = Console()

def main():
    if len(sys.argv) < 2:
        sys.exit("No command provided!")

    command = sys.argv[1]

    if command == 'q':
        sys.exit("Closing prgram..... Done! :D")

    if command in ["complete", "delete"]:
        task = sys.argv[2]
    else:
        task = " ".join(sys.argv[2:])

    if command in ["add", "complete", "delete"] and len(sys.argv) < 3:
        sys.exit("Missing argument!")

    if command == 'add':
        add_task(task)
    elif command == 'list':
        list_task()
    elif command == 'complete':
        complete_task(task)
    elif command == 'delete':
        delete_task(task)
    else:
        print("Enter valid task!")


def add_task(task, filepath='tasks.json'):
    try:
        with open(filepath, 'r') as file:
            tasks = json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        tasks = []
    if not task.strip():
        print("Task cannot be empty!")
        return

    for existing_task in tasks:
        if existing_task['task'].lower() == task.lower():
            print("Task already exists!")
            return

    new_task = {
        'task': task,
        'completed': False,
    }

    tasks.append(new_task)

    with open(filepath, 'w') as file:
        json.dump(tasks, file, indent=4)

    print(f"Task added: {task}")


def list_task(filepath='tasks.json'):
    try:
        with open(filepath, 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Can not show the list unfortunately!")
        return
    if not tasks:
        print("No tasks yet!")
        return

    table = Table(title='Taskr - Task Manager')

    table.add_column('ID')
    table.add_column('Task')
    table.add_column('Status', justify='center')

    for task_id, each_task in enumerate(tasks, start=1):
        status = "✓" if each_task["completed"] else "✗"

        table.add_row(
            str(task_id),
            each_task['task'].title(),
            status
        )
    print("\n")
    console.print(table)


def complete_task(task, filepath='tasks.json'):
    try:
        with open(filepath, 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No tasks found!")
        return

    try:
        index = int(task) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task ID!")
            return
        if tasks[index]['completed']:
            print("Task already completed!")
            return
        tasks[index]['completed'] = True
    except ValueError:
        print("Please enter a valid number!")
        return

    with open(filepath, 'w') as file:
        json.dump(tasks, file, indent=4)

    print(f"Task completed: {task}")


def delete_task(task, filepath='tasks.json'):
    try:
        with open(filepath, 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No tasks found!")
        return

    try:
        index = int(task) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task ID!")
            return
        tasks.pop(index)
    except ValueError:
        print("Please enter a valid number!")
        return

    with open(filepath, 'w') as file:
        json.dump(tasks, file, indent=4)

    print(f"Task deleted: {task}")


if __name__ == "__main__":
    main()
