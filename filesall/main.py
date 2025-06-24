from functions import get_todos,write_todos
import time
now = time.strftime("%b %d ,%Y %H:%M:%S")
print("It is", now)
while True:
      user_prompt = "Type add,show,edit,,complete,or exit:"
      action = input(user_prompt)

      if action.startswith("add"):
              #todo = input("enter a todo :") + "\n"
              todo = action[4:] + "\n"
              #file = open("todos.txt", "r")
              #todos = file.readlines()
              #file.close()
              todos = get_todos()

              todos.append(todo)
              #file = open("todos.txt","w")
              #file.writelines(todos)
              #file.close()
              write_todos("todos.txt", todos)
      elif  action.startswith("show"):#bitwise or operator
              #file = open("todos.txt","r")
              #todos = file.readlines()
              #file.close()
              todos = get_todos()

              for index,i in enumerate(todos):
                   #i = i.title()
                   #print(index+1,".",i.title())
                   i = i.strip('\n')
                   print("{}.{}".format(index+1,i.title()))
      elif action.startswith("edit"):
           try:
             todos = get_todos()
             #n = int(input("enter at which place you want to edit :"))
             new_todo = input("enter a new todo :") + "\n"
             n = int(action[5:])
             todos[n-1] = new_todo
             write_todos("todos.txt", todos)
           except ValueError:
               print("invalid input")
               continue
      elif action.startswith("complete"):
            try:
                todos = get_todos()
                #n1= int(input("enter at which place you want to complete :"))
                n1 = int(action[9:])
                todo_to_be_removed = todos[n1 - 1].strip('\n')
                todos.pop(n1-1)
                write_todos("todos.txt", todos)
                message = f"Todo {todo_to_be_removed} has been removed."
                print(message)
            except (IndexError,ValueError) as e:
                if type(e) == IndexError:
                    print("invalid item out of range")
                else:
                    print("Invalid input")
                continue

                continue
      elif action.startswith("exit"):
               break
      else:
          print(f"{action} is not a valid action.")
for index,item in enumerate(todos,start=1):
    row = f"{index}. {item}"
    print(row)

