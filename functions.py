"""Functions to manipulate files(read & write)"""

FILEPATH = "todo.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return list of
     to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write to-dos in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())
    print("hello")
