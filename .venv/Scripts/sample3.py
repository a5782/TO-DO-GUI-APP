temperatures = ["10\n", "12\n", "14\n"]

file = open("file.txt", 'w')

file.writelines(temperatures)
file.writelines(temperatures[])