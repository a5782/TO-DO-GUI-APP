import functions
import FreeSimpleGUI

label = FreeSimpleGUI.Text("Type to-do in app")
input_box = FreeSimpleGUI.InputText(tooltip="enter todo",key="todo")
add_button = FreeSimpleGUI.Button("Add")
#label1 = FreeSimpleGUI.Text("Type to-do today")
#input_box1 = FreeSimpleGUI.InputText(tooltip="enter todo")
window = FreeSimpleGUI.Window("My To-Do App",
                              layout=[[label],[input_box,add_button]])
while True:
      event,values = window.read()
      print(event)
      print(values)
      match event:
          case "Add":
              todos = functions.get_todos("todos.txt")
              new_todo = values['todo'] + '\n'
              todos.append(new_todo)
              functions.write_todos("todos.txt",todos)
              #print(event)
              #print(values)
          case FreeSimpleGUI.WINDOW_CLOSED:
              break
window.close()