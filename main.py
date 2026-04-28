"""Laboratorio 8 - CLI del gestor de tareas."""
import sys
from todo_manager import read_todo_file, write_todo_file

try:
    if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided!")
    if sys.argv[1] == "--help":
        print("""Usage: python main.py <file_path> <command> [arguments]...

Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.

Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
        sys.exit()
    file_path = sys.argv[1]
    if len(sys.argv) == 2:
        sys.exit()
    tasks = read_todo_file(file_path)

    i = 2

    while i < len(sys.argv):

        command = sys.argv[i]

        if command == "view":

            print("Tasks:")
            for task in tasks:
                print(task)

            i += 1
        elif command == "add":

            if i + 1 >= len(sys.argv):
                raise IndexError('Task description required for "add".')

            new_task = sys.argv[i + 1]

            tasks.append(new_task)

            print(f'Task "{new_task}" added.')

            i += 2

        elif command == "remove":

            if i + 1 >= len(sys.argv):
                raise IndexError('Task description required for "remove".')

            remove_task = sys.argv[i + 1]

            try:
                tasks.remove(remove_task)
                print(f'Task "{remove_task}" removed.')

            except ValueError:
                print(f'Task "{remove_task}" not found.')

            i += 2
        else:
            raise ValueError("Command not found!")
    write_todo_file(file_path, tasks)
except IndexError as e:
    if str(e) == "":
        print("Insufficient arguments provided!")
    else:
        print(e)

except ValueError as e:
    print(e)