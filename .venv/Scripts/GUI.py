import functions
import FreeSimpleGUI
import time


FreeSimpleGUI.theme("Black")    
clock = FreeSimpleGUI.Text(" ",key="clock")
label = FreeSimpleGUI.Text("Type to-do in app")
input_box = FreeSimpleGUI.InputText(tooltip="enter todo",key="todo")
add_button = FreeSimpleGUI.Button("Add")
#label1 = FreeSimpleGUI.Text("Type to-do today")
#input_box1 = FreeSimpleGUI.InputText(tooltip="enter todo")
list_box = FreeSimpleGUI.Listbox(values=functions.get_todos("todos.txt"),enable_events=True,size =[45,10],key="todos")
edit_button = FreeSimpleGUI.Button("Edit")
complete_button = FreeSimpleGUI.Button("complete")
exit_button = FreeSimpleGUI.Button("Exit")
window = FreeSimpleGUI.Window("My To-Do App",
                              layout=[[clock],
                                      [label],[input_box,add_button],
                                      [list_box,edit_button,complete_button],
                                      [exit_button]],)


while True:
      event,values = window.read(timeout=200)
      window["clock"].update(value=time.strftime("%b %d %H:%M:%S"))
      print(event)
      print(values)
      match event:
          case "Add":
              todos = functions.get_todos("todos.txt")
              new_todo = values['todo'] + '\n'
              todos.append(new_todo)
              functions.write_todos("todos.txt",todos)
              window['todos'].update(values=todos)
              #print(event)
              #print(values)
          case "Edit":
              try:
                  todos = functions.get_todos("todos.txt")
                  todo_to_edit = values['todos'][0]
                  new_todo = values['todo'] + '\n'
                  n = todos.index(todo_to_edit)
                  todos[n] = new_todo
                  functions.write_todos("todos.txt", todos)
                  window['todos'].update(values=todos)
              except IndexError:
                     #print("Please select an item first")
                     FreeSimpleGUI.popup("Please select an item first")
          case "todos":
              window['todo'].update(value=values['todos'][0])
          case "complete":
              try:
                   todos = functions.get_todos("todos.txt")
                   todo_to_complete = values['todos'][0]
                   #todos.remove(todo_to_complete)
                   n = todos.index(todo_to_complete)
                   todos.pop(n)
                   functions.write_todos("todos.txt",todos)
                   window['todos'].update(values=todos)
                   window['todo'].update(value=" ")
              except IndexError:
                  FreeSimpleGUI.popup("Please select an item_to_complete first")
          case "Exit":
              break

          case FreeSimpleGUI.WINDOW_CLOSED:
              break
window.close()
