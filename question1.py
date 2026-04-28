"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

import sys

def main():
    try:
        if len(sys.argv) != 3:
            raise ValueError

        total_load = float(sys.argv[1])
        num_supports = float(sys.argv[2])

        if num_supports == 0:
            print("Error: Cannot divide by zero! Supports must be greater than zero.")
            return
        load_per_support = total_load / num_supports

        print(f"Load per support point: {load_per_support:.2f} N")

    except ValueError:
        print("Error: Invalid input! Enter numeric values only.")

if __name__ == "__main__":
    main()

file_name = "tasks.txt"

def load_tasks():
    tasks = []
    try:
        file = open(file_name, "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            tasks.append(line.strip())

    except FileNotFoundError:
        tasks = []

    return tasks

def save_tasks(tasks):
    file = open(file_name, "w")

    for task in tasks:
        file.write(task + "\n")

    file.close()

def view_tasks():
    tasks = load_tasks()

    if tasks == []:
        print("No tasks found.")
        return

    print("Your Tasks:")

    i = 1
    for task in tasks:
        print(str(i) + ". " + task)
        i = i + 1

def add_task(task):
    tasks = load_tasks()

    tasks.append(task)

    save_tasks(tasks)

    print("Task added successfully.")

def remove_task(number):
    tasks = load_tasks()

    try:
        index = int(number)

        if index < 1 or index > len(tasks):
            print("Error: Invalid task number.")
            return

        removed_task = tasks.pop(index - 1)

        save_tasks(tasks)

        print("Removed task: " + removed_task)

    except ValueError:
        print("Error: Invalid input! Enter a valid task number.")

def main():

    if len(sys.argv) < 2:
        print("Usage:")
        print("python question1.py view")
        print("python question1.py add \"Task name\"")
        print("python question1.py remove <task_number>")
        return

    command = sys.argv[1]

    if command == "view":
        view_tasks()

    elif command == "add":

        if len(sys.argv) < 3:
            print("Error: Missing task description.")
            return

        task = sys.argv[2]

        add_task(task)

    elif command == "remove":

        if len(sys.argv) < 3:
            print("Error: Missing task number.")
            return

        remove_task(sys.argv[2])

    else:
        print("Error: Unknown command.")


main()