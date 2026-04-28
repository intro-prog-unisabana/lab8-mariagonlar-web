"""Laboratorio 8 - CLI del gestor de tareas."""
import sys
from todo_manager import read_todo_file, write_todo_file
try:
    file_path = sys.argv[1]
    print("Command-line arguments:")
    i = 1
    while i < len(sys.argv):
        print(sys.argv[i])
        i = i + 1
    tasks = read_todo_file(file_path)
    print("\nTasks:")
    for task in tasks:
        print(task)
except IndexError:
    print("Insufficient arguments provided!")
