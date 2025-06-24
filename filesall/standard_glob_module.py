import glob
from functions import get_todos
myfiles = glob.glob("*.txt")  #filter operations
print(myfiles)
for filename in myfiles:
    #with open(filename, "r") as file:
     #   content = file.readlines()
      content  = get_todos(filename)
      print(content)
