while True:
      user_prompt = "Type add,show,edit,,complete,or exit:"
      action = input(user_prompt)

      if "add" in action:
              #todo = input("enter a todo :") + "\n"
              todo = action[4:] + "\n"
              #file = open("todos.txt", "r")
              #todos = file.readlines()
              #file.close()
              with open("todos.txt","r") as file:
                  todos = file.readlines()

              todos.append(todo)
              #file = open("todos.txt","w")
              #file.writelines(todos)
              #file.close()
              with open("todos.txt","w") as file:
                    file.writelines(todos)
      elif  "show"  in action:#bitwise or operator
              #file = open("todos.txt","r")
              #todos = file.readlines()
              #file.close()
              with open("todos.txt","r") as file:   #context manager
                  todos = file.readlines()

              for index,i in enumerate(todos):
                   #i = i.title()
                   #print(index+1,".",i.title())
                   i = i.strip('\n')
                   print("{}.{}".format(index+1,i.title()))
      elif "edit" in action:
            with open("todos.txt","r") as file : todos = file.readlines()
            #n = int(input("enter at which place you want to edit :"))
            new_todo = input("enter a new todo :") + "\n"
            n = int(action[5:])
            todos[n-1] = new_todo
            with open("todos.txt","w") as file: file.writelines(todos)
      elif "complete" in action:
            with open("todos.txt","r") as file: todos = file.readlines()
            #n1= int(input("enter at which place you want to complete :"))
            n1 = int(action[9:])
            todo_to_be_removed = todos[n1 - 1].strip('\n')
            todos.pop(n1-1)
            with open("todos.txt","w") as file: file.writelines(todos)
            message = f"Todo {todo_to_be_removed} has been removed."
            print(message)
      elif "exit" in action:
               break
      else:
          print(f"{action} is not a valid action.")
for index,item in enumerate(todos,start=1):
    row = f"{index}. {item}"
    print(row)

