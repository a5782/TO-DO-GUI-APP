def get_todos(Filepath):
    with open(Filepath, "r") as file:
        todos_local = file.readlines()
        return todos_local
def write_todos(filepath,todos_arg):
    with open("todos.txt", "w") as file:
        file.writelines(todos_arg)

'''
print(__name__)
if __name__ == '__main__':
    print("Hello World")
    '''