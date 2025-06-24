import functions
import FreeSimpleGUI

label = FreeSimpleGUI.Text("Type to-do in app")
input_box = FreeSimpleGUI.InputText(tooltip="enter todo")
add_button = FreeSimpleGUI.Button("Add")
label1 = FreeSimpleGUI.Text("Type to-do today")
input_box1 = FreeSimpleGUI.InputText(tooltip="enter todo")
window = FreeSimpleGUI.Window("My To-Do App",layout=[[label],[input_box,add_button],[label1,input_box1]])
window.read()
window.close()