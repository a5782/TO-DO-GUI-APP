date = input("enter today's date : ")
mood = input("how to rate your mood from 1-10? ")
thoughts = input("let your thougths flow:\n ")
print("sgbs")

with open(f"{date}.txt","w") as file:
      file.write(mood + "\n")
      file.write(thoughts)