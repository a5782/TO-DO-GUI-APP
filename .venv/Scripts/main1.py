def get_todos():
    with open("todos.txt", "r") as file:
        todos_local = file.readlines()
        return todos_local

while True:
      user_prompt = "Type add,show,edit,,complete,or exit:"
      action = input(user_prompt).strip()
      match action:
            case "add":
                  todo = input("enter a todo :") + "\n"
                  #file = open("todos.txt", "r")
                  #todos = file.readlines()
                  #file.close()
                  todos = get_todos()


                  todos.append(todo)
                  #file = open("todos.txt","w")
                  #file.writelines(todos)
                  #file.close()
                  with open("todos.txt","w") as file:
                        file.writelines(todos)
            case "show" | "display":#bitwise or operator
                  #file = open("todos.txt","r")
                  #todos = file.readlines()
                  #file.close()
                  todos = get_todos()

                  for index,i in enumerate(todos):
                       #i = i.title()
                       #print(index+1,".",i.title())
                       i = i.strip('\n')
                       print("{}.{}".format(index+1,i.title()))
            case "edit":
                todos = get_todos()
                n = int(input("enter at which place you want to edit :"))
                new_todo = input("enter a new todo :") + "\n"
                todos[n-1] = new_todo
                with open("todos.txt","w") as file: file.writelines(todos)
            case "complete":
                todos = get_todos()
                n1= int(input("enter at which place you want to complete :"))
                todo_to_be_removed = todos[n1 - 1].strip('\n')
                todos.pop(n1-1)
                with open("todos.txt","w") as file: file.writelines(todos)
                message = f"Todo {todo_to_be_removed} has been removed."
                print(message)
            case "exit":
                 break
            case asas:    #by default without commas
                print("enter unknow command")
for index,item in enumerate(todos,start=1):
    row = f"{index}. {item}"
    print(row)